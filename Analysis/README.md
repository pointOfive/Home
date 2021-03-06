# Data Analysis with Python

This page provides the following python-based data analysis examples. To see data analysis work done using the R programming language
please visit the [Model-Based Recursive Partitioning project](https://github.com/pointOfive/Home/tree/master/Code#r)
on the [coding page](https://github.com/pointOfive/Home/tree/master/Code#coding). 

- [Data Pipelining Functionality](#data-pipelining-functionality)
- [Regularized Confidence Intervals](#classical-meets-modern)
- [Interpreting Black-Box Models](#the-black-box-myth)
- [Decision Making with Profit Curves](#the-black-box-myth)
- [The Role of Experimental Design](#interpreting-feature-effects)
- [Setting Model Tuning Parameters](#selecting-model-tuning-parameters)
- [Web Scraping Database Server](#web-scraping-database-server)
- [Spark NLP Clustering Pipeline](#nlp-and-clustering-with-spark)
- [ML Pipeline Production Readiness](#ml-production-readiness)
- [Bayesian Trivariate Regression](#bayes-with-pymc3)
- [Interpreting P-Values Correctly](#afterward-p-values)



## Data Pipelining Functionality

The `Scikit-Learn` `Pipeline` package
facilitates data processing and transformation within a cross validation
context by providing `pipeline` objects that invoke a series of `.transform`
methods as part of `.fit` and `.predict` calls. 
This functionality simplifies and abstracts the
data modeling process, but the capabilities available out of the box
leave some things to be desired; namely, the built-in `Transformer` objects
do not provide the full control that an analyst might require.
I have therefore amended and wrapped these functionalities in my own
`Transformer` class objects which provide 


<details>
<summary>
customized handing of missing data columns
</summary>

<br>

```python
from sklearn.base import BaseEstimator,TransformerMixin
from statsmodels.regression.linear_model import OLS
from statsmodels.api import Logit, add_constant
from sklearn.preprocessing import StandardScaler, Imputer
import pandas as pd
import numpy as np
from scipy import stats
stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)

# checking missingness is a bit tricky
isnan = np.vectorize(lambda x: x == 'nan' if type(x) == str else x is np.nan or np.isnan(x))

class add_missing_indicator(BaseEstimator,TransformerMixin):
    """add missingness column"""

    def __init__(self, colnames, to_be_transformed):
        """np.array: of column names (matching X)                                                                                                             
           list: of column names to be standardized"""
    def __init__(self, colnames, cols_to_change):
        self.colnames = colnames
        self.cols_to_change = cols_to_change

    def fit(self, X, Y=None):
        return self

    def transform(self, X):
        self.endcolnames = self.colnames.copy()
        XX = np.zeros((X.shape[0],X.shape[1]+len(self.cols_to_change)), dtype="object")
        XX[:,:-len(self.cols_to_change)] = X.copy()
        for i,c in enumerate(self.cols_to_change):
            XX[:, X.shape[1]+i] = isnan(X[:,self.colnames==c].flatten())
            self.endcolnames = np.array(self.endcolnames.tolist() + [c+"_missing"])
        return XX

class impute_continuous(BaseEstimator,TransformerMixin):
    """Fill missing with median -- wraps sklearn.Imputer"""

    def __init__(self, colnames, to_be_transformed, power=2):
        """np.array: of column names (matching X)                                                                                                             
           list: of column names to impute missing with median"""
    def __init__(self, colnames, to_be_transformed):
        self.colnames = colnames
        self.to_be_transformed = to_be_transformed.copy()
        self.impute = Imputer(strategy="median")

    def fit(self, X, Y=None):
        Xc = X[:, self.to_be_transformed]
        self.endcolnames = np.array(self.colnames[self.to_be_transformed].tolist() + self.colnames[False == self.to_be_transformed].tolist())
        self.impute.fit(Xc)
        return self

    def transform(self, X):
        Xc = X[:,self.to_be_transformed].copy()
        Xd = X[:, False==self.to_be_transformed].copy()
        Xcc = self.impute.transform(Xc)
        X = np.zeros([Xcc.shape[0],Xcc.shape[1]+Xd.shape[1]], dtype="object")
        X[:,:-Xd.shape[1]] = Xcc
        X[:,Xcc.shape[1]:] = Xd
        return X.astype(float)        
```

</details>


<details>
<summary>
full control of indicator variable creation
</summary>

<br>


```python
class create_indicators(BaseEstimator,TransformerMixin):
    """make indicators out of categorical"""

    def __init__(self, colnames, cols_to_change, thresh, remove):
        """np.array: of column names (matching X)                                                                                                             
           list: of column names to be standardized                                                                                                           
           threshold: minimum number of appearances                                                                                                           
           list of lists: levels to ignore for each column being standardized"""
        self.colnames = colnames
        self.cols_to_change = cols_to_change
        self.thresh = thresh
        self.cols_to_change_levels = []
        self.remove = remove

    def fit(self, X, Y=None):
        fit_df = pd.DataFrame(X, columns=self.colnames)
        for i,c in enumerate(self.cols_to_change):
            tmp = fit_df.groupby(c).size()
            tmp = tmp[tmp>self.thresh[i]].index.tolist()
            tmp = [cc for cc in tmp if cc not in self.remove[i]]
            self.cols_to_change_levels.append(tmp)
        return self

    def transform(self, X):
        self.endcolnames = self.colnames.copy()
        XX = X.copy()
        for i,c in enumerate(self.cols_to_change):
            col = np.arange(len(self.endcolnames))[self.endcolnames==c][0]
            XX = np.zeros((X.shape[0],X.shape[1]+len(self.cols_to_change_levels[i])),dtype="object")
            XX[:,:-len(self.cols_to_change_levels[i])] = X.copy()
            for j,l in enumerate(self.cols_to_change_levels[i]):
                XX[:, X.shape[1]+j] = (XX[:, col] == l).flatten()
                self.endcolnames = np.array(self.endcolnames.tolist() + [c+"_"+str(l)])
            X = XX.copy()
        for c in self.cols_to_change:
            XX = XX[:,self.endcolnames != c].copy()
            self.endcolnames = self.endcolnames[self.endcolnames != c]
        return XX.astype(float)
```

</details>

<details>
<summary>
selective and partial normalization capabilities
</summary>

<br>

```python
class standardize_continuous(BaseEstimator,TransformerMixin):
    """standardize -- wraps sklearn.StandardScaler"""

    def __init__(self, colnames, to_be_transformed):
        """np.array: of column names (matching X)                                                                                                             
           list: of column names to be standardized"""
        self.colnames = colnames
        self.to_be_transformed = to_be_transformed.copy()
        self.standardize = StandardScaler()

    def fit(self, X, Y=None):
        Xc = X[:, self.to_be_transformed]
        self.endcolnames = np.array(self.colnames[self.to_be_transformed].tolist() + self.colnames[False == self.to_be_transformed].tolist())
        self.standardize.fit(Xc)
        return self

    def transform(self, X):
	Xc = X[:,self.to_be_transformed].copy()
        Xd = X[:, False==self.to_be_transformed].copy()
        Xcc = self.standardize.transform(Xc)
        X = np.zeros([Xcc.shape[0],Xcc.shape[1]+Xd.shape[1]], dtype="object")
        X[:,:-Xd.shape[1]] = Xcc
        X[:,Xcc.shape[1]:] = Xd
        return X
```
</details>


<details>
<summary>
simplified higher order interaction specification
</summary>

<br>

```python
class interacts(BaseEstimator,TransformerMixin):
    """Add interactions to feature matrix"""

    def __init__(self, colnames, to_be_transformed):
        """np.array: of column names (matching X)                                                                                                             
           list: of column names to make interactions from"""
        self.colnames = colnames
        self.to_be_transformed = to_be_transformed

    def fit(self, X, Y=None):
        self.endcolnames = self.colnames.tolist()[:]
        for c1 in range(0,len(self.to_be_transformed)):
            for c2 in range(c1+1,len(self.to_be_transformed)):
                if np.std(X[:,np.array(self.colnames) == self.to_be_transformed[c1]]*X[:,np.array(self.colnames) == self.to_be_transformed[c2]]) != 0.0:
                    self.endcolnames.append(self.to_be_transformed[c1]+"_x_"+self.to_be_transformed[c2])
        self.endcolnames = np.array(self.endcolnames)
        return self

    def transform(self, X):
        Xnew = X.copy()
        for c1 in range(0,len(self.to_be_transformed)):
            for c2 in range(c1+1,len(self.to_be_transformed)):
                if self.to_be_transformed[c1]+"_x_"+self.to_be_transformed[c2] in self.endcolnames:
                    tmp = X[:,np.array(self.colnames) == self.to_be_transformed[c1]]*X[:,np.array(self.colnames) == self.to_be_transformed[c2]]
                    Xnew=np.concatenate([Xnew, tmp], axis=1)
        return Xnew

class add_higher_orders(BaseEstimator,TransformerMixin):
    """Add higher order terms to feature matrix"""

    def __init__(self, colnames, to_be_transformed, power=2):
        """np.array: of column names (matching X)                                                                                                             
           list: of column names to make powers of                                                                                                            
           power: higher order to add"""
        self.colnames = colnames
        self.to_be_transformed = to_be_transformed
        self.power = power

    def fit(self, X, Y=None):
        self.endcolnames = self.colnames.tolist()[:]
        for c in self.to_be_transformed:
            for p in range(2,self.power+1):
                self.endcolnames.append(c+"_"+str(p))
        self.endcolnames = np.array(self.endcolnames)
        return self

    def transform(self, X):
        Xnew = X.copy()
        for c in self.to_be_transformed:
            for p in range(2,self.power+1):
                Xnew=np.concatenate([Xnew, X[:,np.array(self.colnames) == c]**p], axis=1)
        return Xnew
```
</details>




<details>
<summary>
access to classical statistical methodologies
</summary>

<br>

```python
class SMLR(object):
    """wraps statsmodels.logistic_regression"""

    def __init__(self, colnames, drop, alpha=0):
        """np.array: of column names (matching X)                                                                                                             
           list: referent group columns (to drop)                                                                                                             
           regulariztion: 0 is none"""
        self.colnames = colnames
        self.drop = drop
        self.alpha = alpha

    def fit(self, Xdat, Ydat):
        Xdat = pd.DataFrame(Xdat.astype(float),columns=self.colnames)
        Xdat = add_constant(Xdat, has_constant='add')
        for c in self.drop:
            del Xdat[c]
        self.model = Logit(Ydat, Xdat)
        self.results = self.model.fit_regularized(method='l1', alpha=np.array([0]+[self.alpha]*(Xdat.shape[1]-1)),trim_mode='off')
        return self

    def predict_proba(self, Xdat=None):
        tmp = self.predict(Xdat)
        return np.array([1-tmp,tmp]).T

    def predict(self, Xdat=None):
        if Xdat is None:
            return self.results.predict()
        else:
            Xdat = pd.DataFrame(Xdat.astype(float),columns=self.colnames)
            Xdat = add_constant(Xdat, has_constant='add')
            for c in self.drop:
                del Xdat[c]
            return self.results.predict(exog=Xdat)

class SMOLS(object):
    """wraps statsmodels.OLS_regression"""

    def __init__(self, colnames):
        """np.array: of column names (matching X)                                                                                                             
           [TO BE ADDED] list: referent group columns (to drop)                                                                                               
           [TO BE ADDED] regulariztion: 0 is none"""

    def __init__(self, colnames):
        self.colnames = colnames

    def fit(self, Xdat, Ydat):
        Xdat = pd.DataFrame(Xdat,columns=self.colnames)
        for c in self.drop:
            del Xdat[c]
        Xdat = add_constant(Xdat, has_constant='add')
        self.model = OLS(Ydat, Xdat, hasconst=True)
        self.results = self.model.fit()
        return self

    def predict(self, Xdat=None):
        if Xdat is None:
            return self.results.predict()
        else:
            Xdat = pd.DataFrame(Xdat,columns=self.colnames)
            Xdat = add_constant(Xdat, has_constant='add')
            for c in self.drop:
                del Xdat[c]
            return self.results.predict(exog=Xdat)

class pipelined_data(object):
    """end of pipeline placeholder to hold transformed X"""

    def __init__(self):
        pass

    def fit(self, X, Y):
        self.X = X
        return self
```

</details>

<br>

With these tools data processing pipelines are initialized as follows: 

```python
from pipeline import *
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np

Ydat = dat[[outcome]].copy()
Xdat = dat[features].copy()

# preprocessing
addmiss = add_missing_indicator(Xdat.columns, features_wMissingness)
Xdat = addmiss.transform(Xdat.as_matrix())

onehot = create_indicators(addmiss.endcolnames, features_wCategories, thresh=[5]*2, remove=levels2ignore)
onehot.fit(Xdat)
Xdat = onehot.transform(Xdat)

XdatSAVE = Xdat.copy()

# training processing
fillWmedian = impute_continuous(onehot.endcolnames, np.array([c in features_4medianImputation for c in onehot.endcolnames]))
fillWmedian.fit(Xdat)
Xdat = fillWmedian.transform(Xdat)

scale_conts = standardize_continuous(fillWmedian.endcolnames, np.array([c in features_4standardization for c in fillWmedian.endcolnames]))
scale_conts.fit(Xdat)
Xdat = scale_conts.transform(Xdat)

# classical model building
synergize = interacts(scale_conts.endcolnames, list(set(scale_conts.endcolnames).difference(set(features_2notInteract+[c for c in scale_conts.endcolnames if '_missing' in c]))))
synergize.fit(Xdat)
Xdat = synergize.transform(Xdat)

powers = add_higher_orders(np.array(synergize.endcolnames), features_4higherOrder,2)
powers.fit(Xdat)
Xdat = powers.transform(Xdat)
```

And then and used as follows:

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

get_data = pipelined_data()
data_pipeline = Pipeline([('fillWmedian',fillWmedian), ('scale_conts',scale_conts), ('get_data',get_data)])
data_pipeline.fit(Xdat, Ydat.as_matrix()[:,0])
Xdat = data_pipeline.named_steps['get_data'].X.astype(float)

rf = RandomForestClassifier(min_weight_fraction_leaf = 0.05, max_features=.4, n_estimators=100)
rf_pipeline = Pipeline([('fillWmedian',fillWmedian), ('scale_conts',scale_conts), ('rf',rf)])
rf_pipeline.fit(Xdat, Ydat.Y.values)

lr = SMLR(powers.endcolnames, features_2notInteract+remove, 0) 
lr_full_pipeline = Pipeline([('fillWmedian',fillWmedian), ('scale_conts',scale_conts), ('synergize', synergize), ('powers', powers), ('lr',lr)])
lr_full_pipeline.fit(Xdat, Ydat.Y.values)

svc = svm.SVC(C=10, gamma=.005, probability=True)
svc_pipeline = Pipeline([('fillWmedian',fillWmedian), ('scale_conts',scale_conts), ('svc',svc)])
svc_pipeline.fit(Xdat[samp,:], Ydat.as_matrix()[samp,0])
```


## Classical meets Modern

The final two custom data pipelining functionalities 
concern themselves with "classical" exercises specific to `Linear Model` operationalization, 
but they allow us to carry desirable statistical analysis capabilities forward into
the modern supervised learning framework. The following example demonstrates the
synergistic integration of regularization and uncertainty quantification
in the context of multiplicative association identification in classification settings.
Click on the plot or [this link](http://ec2-3-85-212-72.compute-1.amazonaws.com/#regularized_confidence_intervals) to explore the live interactive version
of the plot. 

<p align="center">
<a href="http://ec2-3-85-212-72.compute-1.amazonaws.com/#regularized_confidence_intervals"><img src="images/regularize.jpeg"/></a>
</p>

Methodologies such as `Random Forests`,
`Support Vector Machines` (via the `Kernel Trick`), and `Gradient Boosted Trees`
automatically leverage extremely complex higher order interaction associations, but
any higher order interaction associations to be considered in the context of
`Linear Models` require explicit *a priori* specification and construction.
As a result, `Linear Model` specifications cannot realistically consistently compete with
the modeling flexibility provided by modern predictive machine learning methodologies; however, 
the statistical analysis capabilities available
within a `Linear Model` framework serve to ensure
it's competitiveness as an analytical tool by
providing uncertainty characterizations
that can be brought to bear on questions of model building and interpretation.


## The "Black-Box" Myth

A frequent charge leveled against modern machine learning predictive methodologies is that
they are not interpretable the way a `Linear Model` frameworks is.
This is patently incorrect for the following two reasons:

- the venerable *"hold all but one feature constant"* standard `Linear Model` interpretation
is available in all contexts as a so-called *Partial Dependency Plot*
- examinations of the presence of specific interactions requires their explicit construction,
and can be carried out on the basis of *Feature Importance Diagnostics* -- not only via hypothesis testing

The following example demonstrates the former *Partial Dependency Plots* for the
`Logistic Regression`, `Random Forest`, and `Support Vector Machine` classifier pipelines above.
In addition the `Gradient Boosted Tree` classifier from the `XGBoost` package is also provided
for further comparison.
Click on the plot or [this link](http://ec2-3-85-212-72.compute-1.amazonaws.com/#association_plots) to explore the live interactive version
of the plot.

<p align="center">
<a href="http://ec2-3-85-212-72.compute-1.amazonaws.com/#association_plots"><img src="images/effects.jpeg"/></a>
</p>

The actual predicted associations -- i.e., per-person individualized effects -- are given in the upper right plot,
and a comparison between the predicted values of the methodologies is given in the lower right plot.
The feature interpretation similarities between the different methodologies are notable, while the individual prediction discrepancies
look well suited to exploitation via [model stacking](https://www.quora.com/What-is-stacking-in-machine-learning)
(for the purpose of attempting to balance and tradeoff the strengths of each within a multi-layer model framework).
Gradient boosted tree classifier capabilities are provided follows: 
```python
import xgboost as xgb
progress=dict()
param = {'max_depth':2, 'eta':.01, 'subsample': .001, 'silent':True, 'objective':'binary:logistic', 'eval_metric':['error','logloss']}
bst = xgb.train(param, dtrain, num_round, [(dtrain, 'train'), (dtest, 'eval')], evals_result=progress, early_stopping_rounds=5/(sub_sample**.6*learning_rate**.25), verbose_eval=False)      
bst.predict(dtrain, ntree_limit=bst.best_ntree_limit)
```



## Model-Based Decision Making

Model interpretation does not factor into prediction-based decision making.
When models are used for purely predictive purposes it does not matter
if there is confounding (observed or otherwise) and if ([as discussed in the next section](#interpreting-feature-effects)) 
this limits the ability to attribute and interpret associations to specific features
within the context of the model: all that matters is raw predictive performance.
The following example demonstrates *profit curves* based on *cost-benefit* and *confusion matrices*.
Specification of the cost-benefit allows us to tune our *classification threshold* to optimize
the interplay of the *confusion* and *cost-benefit matrices*.
Click on the plot or [this link](http://ec2-3-85-212-72.compute-1.amazonaws.com/#cost_benefit) to explore the live interactive version
of the plot.

<p align="center">
<a href="http://ec2-3-85-212-72.compute-1.amazonaws.com/#cost_benefit"><img src="images/costbenefit.jpeg"/></a>
</p>



## Interpreting "Feature Effects"

The real issue in interpreting feature-outcome associations comes down to *experimental design*;
specifically, it is feature correlation which limits association attribution and the ever present
risk of actual confounding that renders associations non causative.
Of course if [interest lies in prediction alone this is immaterial](#model-based-decision-making).
But if interest lies in ["interpretation of feature effect"](#the-black-box-myth) then
for all models -- flexible `Supervised Machine Learning Models` just as much as `Linear Models` -- 
one must be intentional with sampling across features in order to provide uncorrelated
features and hence unconfounded association interpretation.
*Multicollinearity Structure*, particularly the kind affecting `Linear Models` can be examined through
*Variance Inflation Factors* and *Principal Components Analysis* (and the latter provides
the attractive approach to address correlated features through *Principal Components Regression*).


<p align="center">
<table> <tr> <td><img src="images/pca1.jpeg"/></td> <td><img src="images/pca2.jpeg"/></td> </tr> </table>
</p>


Pairwise correlations are also worth examining directly. For example,
correlated features directly compete for association attribution in
tree based ensembles.
But any model fit in the presence of associations between features
will estimate association attributions as "tradeoffs" between associated features;
thus, associations are not estimated on a *"hold all but one feature constant"* basis
and interpreting them as such is incongruous. 
Principal components analysis and variance inflation factors
are readily available as follows:

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

kp = [False if c in features_2notInteract else True for c in scale_conts.endcolnames]
VIFs = [0]*sum(kp)
for c in range(len(VIFs)):
    VIFs[c] = variance_inflation_factor(Xdat[:,kp],c)

U, s, V = np.linalg.svd(Xdat, full_matrices=False)
scree = np.cumsum(s**2/np.sum(s**2))
```





## Selecting Model Tuning Parameters

Modern predictive methodology avoids overfitting 
by using cross validation techniques to identify appropriate regularization levels.
The `Kfolds` and `GridSearchCV` functionalities in `Scikit-Learn` greatly
facilitate and simplify this task.  

<p align="center">
<img src="images/svc.jpg"/>
</p>

<details>
<summary>
Example K-folds Cross Validation and Grid Search Functionality is available to see here
</summary>

<br>

```python
from sklearn.model_selection import KFold, GridSearchCV

pars={'rf__min_weight_fraction_leaf':np.linspace(.005,.05,10), 'rf__max_features':np.linspace(.1,1,10)}
models = GridSearchCV(estimator=rf_pipeline, param_grid=pars, cv=2, scoring='accuracy', return_train_score=True)
models.fit(Xdat, Ydat.Y.values)

samp=np.random.choice(range(Xdat.shape[0]),5000,replace=False)
Xdat = Xdat[samp,:]
parameters = {'svc__gamma': np.logspace(start=-5,stop=0,base=10,num=num), 'svc__C': np.logspace(start=-1,stop=4,base=10,num=num)}
models = GridSearchCV(estimator=svc_pipeline, param_grid=parameters, cv=2, scoring='accuracy')
models.fit(Xdat, Ydat.as_matrix()[samp,0])

kf = KFold(n_splits=5, random_state=0, shuffle=True)
for learning_rate in [.01,.1]:
    for sub_sample in [.001,.01,.1]:     
        for train_index, test_index in kf.split(Xdat):
            X_train, X_test = Xdat[train_index], Xdat[test_index]
            y_train, y_test = Ydat.as_matrix()[train_index,0], Ydat.as_matrix()[test_index,0]
            dtrain = xgb.DMatrix(X_train, label=y_train)
            dtest = xgb.DMatrix(X_test, label=y_test)
            param = {'max_depth':2, 'eta':learning_rate, 'subsample': sub_sample, 'silent':True, 'objective':'binary:logistic', 'eval_metric':['error','logloss']}
            progress=dict()
            bst = xgb.train(param, dtrain, num_round, [(dtrain, 'train'), (dtest, 'eval')], evals_result=progress, early_stopping_rounds=5/(sub_sample**.6*learning_rate**.25), verbose_eval=False)      
```
</details>

<br>

As models become more flexible they can naturally find more complex generalizations; however,
they also begin to pick up spurious idiosyncrasies in the data.
So while they improve in some parts of the feature space, they begin to overfit in others.
This becomes a question of diminishing appropriate out of sample generalizations in the face of increasing in sample over generalization.
One position on this issue is to increase out of sample prediction regardless.
The implications of this are that 
- increased error due to model variance is allowed while corresponding model bias and residual error reduction is beneficial
- but increased model variance implies overfitting and thus a lack of generalization in model interpretation

The following shows increasing gains in predictive power along with simultaneous increases in demonstrable overfitting, i.e.,
a decreasing ability to generalize predictive gains. 

<p align="center">
<img src="images/gbtc.jpg"/>
</p>


Using *Bagging* to reduce localized spurious overfitting seems like a very promising technique to address this issue, and similarly,
the application of *Bootstrapping* techniques to provide association attribution uncertainty quantification (i.e., "effects uncertainty estimation")
seems like a likewise enticing endeavor. 
Regardless, the intention to equalize in and out of sample testing scores for the purposes of
generalizability of interpretation remains an alternative objective to maximum predictive power.
Again, the motivation behind such an objective is an interest in identifying reproducible
associations, and in particular being willing to reduce the complexity of associations under consideration when the
available data does not sufficiently justify the inference. 
The following example sorts in and out of sample scores by their difference,
and allows the user to hover over the plots to facilitate identification of appropriate tuning parameter settings.
Click on the plot or [this link](http://ec2-3-85-212-72.compute-1.amazonaws.com/#tuning) to explore the live interactive version
of the plot.

<p align="center">
<a href="http://ec2-3-85-212-72.compute-1.amazonaws.com/#tuning"><img src="images/hover.jpg"/></a>
</p>



## Web Scraping Database Server

I built a server to populate target webpages in a database using `selenium` and `psycopg2`. 
The server executed the following two tasks:

<details>
<summary>
crawl a website to collect target webpages 
</summary>

<br>

```python
#!/usr/bin/python                                                                                                                                                             
# chmod a+x indeed_psql_server.py                                                                                                                                             
import psycopg2
from bs4 import BeautifulSoup
import re # Regular expressions                                                                                                                                               
import time  # To prevent overwhelming the server between connections                                                                                                         
from collections import Counter # Keep track of our term counts                                                                                                               
from nltk.corpus import stopwords # Filter out stopwords, such as 'the', 'or', 'and'                                                                                          
import pandas as pd # For converting results to a dataframe and bar chart plots                                                                                               
from selenium import webdriver

def skills_info(search, city, state):
    '''Use "+".join for search/city/state; Let's just get 10 jobs from indeed'''
    site = ''.join(['http://www.indeed.com/jobs?q=%22', search, '%22&l=%22', city,'%22%2C+%22', state,'%22'])
    if city is "":
        site = ''.join(['http://www.indeed.com/jobs?q=%22', search, '%22&l=%22', state,'%22'])
    base_url = 'http://www.indeed.com'
    driver = webdriver.PhantomJS()
    driver.get(site)
    num_jobs_area = driver.find_element_by_id('searchCount').text
    job_numbers = re.findall('\d+', num_jobs_area)#.decode('utf-8')) # Extract the total jobs found from the search result                                                     
    if len(job_numbers) > 2: # Have a total number of jobs greater than 1000                                                                                                   
        total_num_jobs = (int(job_numbers[1])*1000) + int(job_numbers[2])
    else:
        total_num_jobs = int(job_numbers[1])
    num_pages = int(total_num_jobs/10) # This will be how we know the number of times we need to iterate over each new                                                         
    print(num_pages)
    job_URLS, cities, states = [], [], []
    job_link_area = driver.find_elements_by_xpath('//div[@class="  row  result"]')
    time.sleep(1)
    job_link_area = job_link_area + driver.find_elements_by_xpath('//div[@class="lastRow  row  result"]')
    time.sleep(1)
    job_URLS = job_URLS + [link.find_element_by_tag_name('a').get_attribute("href") for link in job_link_area]
    cities = cities + [(loc.find_element_by_xpath('.//span[@class="location"]').text+",").split(",")[0] for loc in job_link_area]
    states = states + [(loc.find_element_by_xpath('.//span[@class="location"]').text+",").split(",")[1] for loc in job_link_area]
    driver.find_element_by_xpath('//div[@class="pagination"]').find_elements_by_tag_name('a')[-1].click()
    cont = True
    while cont:
        job_link_area = driver.find_elements_by_xpath('//div[@class="  row  result"]')
        job_link_area = job_link_area + driver.find_elements_by_xpath('//div[@class="lastRow  row  result"]')
        job_URLS = job_URLS + [link.find_element_by_tag_name('a').get_attribute("href") for link in job_link_area]
        cities = cities + [(loc.find_element_by_xpath('.//span[@class="location"]').text+",").split(",")[-1] for loc in job_link_area]
        states = states + [(loc.find_element_by_xpath('.//span[@class="location"]').text+",").split(",")[1] for loc in job_link_area]
        print(len(set(job_URLS)), len(job_URLS), len(states), len(cities))
        if len(driver.find_elements_by_xpath('//span[@class="np"]')) < 2:
            break
        try:
            driver.find_element_by_xpath('//div[@class="pagination"]').find_elements_by_tag_name('a')[-1].click()
        except:
            cont = False
    return job_URLS, cities, states

```
</details>

<details>
<summary>
host and populate a database of target webpages
</summary>

<br>

```python

conn = psycopg2.connect(dbname='indeed',port=5432, password="postgres", user='postgres',host='localhost')
cur = conn.cursor()

try:
    query = '''CREATE TABLE addresses (path CHARACTER VARYING PRIMARY KEY, search CHARACTER VARYING, city CHARACTER VARYING, state CHARACTER VARYING);'''
    cur.execute(query)
    conn.commit()
except:
    conn.rollback()

try:
    query = '''CREATE TABLE posts (path CHARACTER VARYING PRIMARY KEY, search CHARACTER VARYING, city CHARACTER VARYING, state CHARACTER VARYING, post CHARACTER VARYING, acqu\
ired TIMESTAMP DEFAULT current_timestamp);'''
    cur.execute(query)
except:
    conn.commit()

query = "DELETE FROM posts WHERE post IS NULL;"
cur.execute(query)
conn.commit()
query = "DELETE FROM posts WHERE post = '';"
cur.execute(query)
conn.commit()

query = "SELECT path FROM posts;"
cur.execute(query)
previous = set([r[0] for r in cur])

phrase = "data+science"
loc_city = ("New+York+City", "San+Francisco", "Seattle",    "Washington", "",              "Los+Angeles", "San+Diego",  "Portland", "",      "",         "",         "",      \
  "",                "",         "",            "")
loc_state = ("New+York",     "California",    "Washington", "DC",         "Massachusetts", "California",  "California", "Oregon",   "Texas", "Illinois", "Colorado", "Georgia"\
, "North+Carolina", "Tennessee", "Connecticut", "Pennsylvania")


for j in range(len(loc_city)):
#if 1==1:                                                                                                                                                                     
    print(loc_city[j], loc_state[j])
    pp, c, s = skills_info(phrase, loc_city[j], loc_state[j])
    for i,p in enumerate(pp):
        if p not in previous:
            query = "INSERT INTO addresses (path, search, city, state) VALUES ('" + p + "','" + phrase + "','" + c[i] + "','" + s[i] + "');"
            try:
                cur.execute(query)
                conn.commit()
            except:
                print(query)
                conn.rollback()

cur.close()
conn.close()
```
</details>

<br>

I additionally built a web scraper which could be run simultaneously from different worker nodes.
Worker nodes had two tasks: 

<details>
<summary>
quietly and politely scrape data from a webpage
</summary>

<br>

```python
#!/usr/bin/python
import psycopg2
from bs4 import BeautifulSoup
import re # Regular expressions                                                                                                                                               from time import sleep # To prevent overwhelming the server between connections                                                                                               from collections import Counter # Keep track of our term counts                                                                                                               from nltk.corpus import stopwords # Filter out stopwords, such as 'the', 'or', 'and'                                                                                          import pandas as pd # For converting results to a dataframe and bar chart plots                                                                                               from selenium import webdriver
import os
import time

def text_cleaner(website):
    '''                                                                                                                                                                           This function just cleans up the raw html so that I can look at it.                                                                                                       
    Inputs: a URL to investigate                                                                                                                                                  Outputs: Cleaned text only                                                                                                                                                    '''
    try:
        driver.get(website) #urlopen(website).read() # Connect to the job posting                                                                                                     time.sleep(10)
    except:
        return   # Need this in case the website isn't there anymore or some other weird connection problem                                                                   
    try:
        text = driver.find_element_by_tag_name("body").text
    except:
        return
    lines = (line.strip() for line in text.splitlines()) # break into lines                                                                                                       chunks = (phrase.strip() for line in lines for phrase in line.split("  ")) # break multi-headlines into a line each
    def chunk_space(chunk):
        chunk_out = chunk + ' ' # Need to fix spacing issue                                                                                                                           return chunk_out
    text = ''.join(chunk_space(chunk) for chunk in chunks if chunk).encode('utf-8') # Get rid of all blank lines and ends of line                                                 # Now clean out all of the unicode junk (this line works great!!!)                                                                                                            try:
        text = text.decode('unicode_escape').encode('ascii', 'ignore') # Need this as some websites aren't formatted                                                              except:                                                            # in a way that this works, can occasionally throw                                                             return                                                         # an exception                                                                                             text = text.decode('utf-8')
    return text
    stop_words = set(stopwords.words("english")) # Filter out any stop words                                                                                                      text = [w for w in text if not w in stop_words]
    text = list(set(text)) # Last, just get the set of these. Ignore counts (we are just looking at whether a term existed                                                                                # or not on the website)                                                                                                                           												    
```
</details>

<details>
<summary>
query targets and deliver scraped webpages to the database
</summary>

<br>

```python
conn = psycopg2.connect(dbname='indeed',port=5432, password="postgres", user='postgres',host='ec2-54-210-15-26.compute-1.amazonaws.com')
cur = conn.cursor()
driver = webdriver.PhantomJS()
query = "select COUNT(*) from addresses;"
cur.execute(query)
n = list(cur)[0][0]

while n > 0:
    print(n)
    query = "SELECT * FROM addresses ORDER BY random() LIMIT 10;"
    cur.execute(query)
    posts = list(cur)
    tmp = posts
    for p in tmp:
        try:
            query = "DELETE FROM addresses WHERE path='" + p[0] + "';"
            cur.execute(query)
            conn.commit()
        except:
            conn.rollback()
            print(p)
            posts.remove(p)
    for p in posts:
        path, phrase, city, state = p
        text = text_cleaner(path)
        try:
            tmp = "INSERT INTO posts (path, search, city, state, post) VALUES ('" + path + "','" + phrase + "','" + city + "','" + state + "',%s)"
            cur.execute(tmp, [text])
            conn.commit()
            print("added " + path)
        except:
            print(path)
            conn.rollback()
            print("failed to add " + path)
    query = "select COUNT(*) from addresses;"
    cur.execute(query)
    n = list(cur)[0][0]
    driver.close()
    driver = webdriver.PhantomJS()

cur.close()
conn.close()
```
</details>

<br>


The [server/worker setup](https://github.com/pointOfive/Home/tree/master/Compute#serverworkers-paradigm)
is described on the [computational page](https://github.com/pointOfive/Home/tree/master/Compute#computing).


## NLP and Clustering with Spark

[Notes on setting up a Spark cluster](https://github.com/pointOfive/Home/tree/master/Compute#emr-distributed-computing-paradigm)
are available on the [computational page](https://github.com/pointOfive/Home/tree/master/Compute#computing).
With a spark cluster I made 


<details>
<summary>
an NLP processing pipeline using Spark functionality
</summary>

<br>

```python
from pyspark.sql import Row
from pyspark.sql.functions import udf, col
from pyspark.sql.types import IntegerType, ArrayType, StringType
from pyspark.ml.feature import RegexTokenizer, StopWordsRemover, CountVectorizer, IDF, Normalizer

import unicodedata
from nltk.stem.porter import PorterStemmer

sc = spark.sparkContext
sc.setLogLevel("ERROR")
min_word_lim=100
DSJP = sc.textFile('s3n://bucket/path/file.txt').map(lambda x: unicodedata.normalize('NFKD', str(x))).filter(lambda x: len(x)>min_word_lim).cache()
# remove duplicates
DSJP = sc.parallelize(set(DSJP.collect()))
DSJP.count()

DSJP = DSJP.repartition(20)
DSJP.getNumPartitions()

DSJP_df=spark.createDataFrame(DSJP.map(Row)).toDF('text')
DSJP_df=DSJP_df.filter(~DSJP_df.text.startswith('#REDIRECT')).cache()
DSJP_df.show(3)

countTokens = udf(lambda words: len(words), IntegerType())
regexTokenizer = RegexTokenizer(inputCol="text", outputCol="words", pattern="\\W")
DSJP_df = regexTokenizer.transform(DSJP_df)
DSJP_df = DSJP_df.withColumn("words_wc", countTokens(col("words"))).cache()
DSJP_df.show(3)

sw_remover = StopWordsRemover(inputCol="words", outputCol="woSW")
DSJP_df = sw_remover.transform(DSJP_df)
DSJP_df = DSJP_df.withColumn("woSW_wc", countTokens(col("woSW"))).cache()
DSJP_df.show(3)

def stemmer(word_list):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in word_list]

stemit = udf(stemmer, ArrayType(StringType()))
DSJP_df = DSJP_df.withColumn("stem",stemit(col("woSW"))).cache()
DSJP_df.show(3)

cv = CountVectorizer(inputCol="stem", outputCol="vector_tf", vocabSize=5000, minDF=10)
cv_model = cv.fit(DSJP_df)
len(cv_model.vocabulary)
DSJP_df = cv_model.transform(DSJP_df).cache()
DSJP_df.show(3)

idf = IDF(inputCol="vector_tf", outputCol="vector_tf_idf")
idfModel = idf.fit(DSJP_df)
DSJP_df = idfModel.transform(DSJP_df).cache()
DSJP_df.show(3)

normalizer = Normalizer(inputCol="vector_tf_idf", outputCol="vector_tf_idf_L2", p=2.0)
DSJP_df = normalizer.transform(DSJP_df).select("text", "words", "stem", "vector_tf_idf_L2", "woSW_wc").cache()
DSJP_df.show(3)
```
</details>



<details>
<summary>
an usupervised learniung pipeline using SparkML functionality
</summary>

<br>

```python
from pyspark.ml.clustering import KMeans

import random
import numpy as np
from collections import Counter, defaultdict

# make a markov chain for the null distribution                                                                                                                               
# the idea is to keep the structure of english langue --                                                                                                                      
# -- the marginal markov conditional probability rates accross all documents                                                                                                  
# -- but then beyond that, we want to know if there are *yet further* structures                                                                                              
# within documents that separate them out...                                                                                                                                   
def add(a, b):
    return a+b
    
novel = DSJP_df.select("words").rdd.flatMap(lambda x: x).reduce(add)
mc = defaultdict(list)
mc_order = 5
for i in range(len(novel)-mc_order):
    mc[tuple(novel[i:(i+mc_order)])].append(novel[i+mc_order])

def get_markov_doc(seed, number):
    out = list(seed)
    for i in range(mc_order, number):
        out.append(random.choice(mc[tuple(out[(i-mc_order):i])]))
    return(out)

kmeans = KMeans(k=4, featuresCol="vector_tf_idf_L2", seed=1)
model = kmeans.fit(DSJP_df) # automatically uses the "features" column                                                                                                        
len(model.clusterCenters())
DSJP_df = model.transform(DSJP_df).cache()

# ---------- cluster sizes ---------------
Counter(DSJP_df.select("prediction").rdd.flatMap(lambda x: x).collect())

# ------------- centroids ---------------
# super cool -- gives the dimensions with the highest weights... so what the clusters actually mean...
[[cv_model.vocabulary[i] for i in arr.argsort()[-10:][::-1]] for arr in model.clusterCenters()]

# --------- cluster content --------------
DSJP_df.where("prediction = 0").select("text").rdd.flatMap(lambda x: x).collect()

# -------- doc length in cluster ---------
DSJP_df.where("prediction = 0").select("text","woSW_wc").show()
DSJP_df.where("prediction = 1").select("text","woSW_wc").show()

# -------------choosing k------------------                                                                                                                                   
n = DSJP_df.select("stem").count()

everything = DSJP_df.select("stem").rdd.map(lambda x: x["stem"]).reduce(add)
len(everything)
nulldoc = lambda x: np.random.choice(everything, x).tolist()
nulls = spark.createDataFrame(DSJP_df.select("woSW_wc").rdd.map(lambda x: x['woSW_wc']).map(nulldoc).map(Row)).toDF("stem").cache()
nulls = cv_model.transform(nulls).cache()
nulls = idfModel.transform(nulls).cache()
nulls = normalizer.transform(nulls).select("stem", "vector_tf_idf_L2").cache()
nulls.show()
nulls.count()

nulls = spark.createDataFrame(DSJP_df.select("words").rdd.map(lambda x: x['words']).map(lambda x: get_markov_doc(x[0:mc_order], len(x))).map(Row)).toDF("words").cache()
whatwegot = nulls.select("words").rdd.flatMap(lambda x: x).map(lambda x: " ".join(x)).collect()
actuals = DSJP_df.select("words").rdd.flatMap(lambda x: x).map(lambda x: " ".join(x)).collect()
nulls = sw_remover.transform(nulls)
nulls = nulls.withColumn("woSW_wc", countTokens(col("woSW"))).cache()
nulls = nulls.withColumn("stem",stemit(col("woSW"))).cache()
nulls = cv_model.transform(nulls).cache()
nulls = idfModel.transform(nulls).cache()
nulls = normalizer.transform(nulls).select("stem", "vector_tf_idf_L2").cache()
nulls.show()

# -------------Gap Statistics------------------                                                                                                                       
random.seed(1)
nul_score_mean = []
for k in range(2, 50, 2):
    nul_score = []
    for j in range(10):
        DSJP_df2 = nulls
        kmeans = KMeans(k=k, featuresCol="vector_tf_idf_L2", seed=random.randint(1,1000000))#, seed=1)                                                                         
        model = kmeans.fit(DSJP_df2)
        DSJP_df2 = model.transform(DSJP_df2)
        clusterCenters = model.clusterCenters()
        nul_score.append(DSJP_df2.select("prediction").rdd.flatMap(lambda x: x).\
                         zip(DSJP_df.select("vector_tf_idf_L2").rdd.flatMap(lambda x: x)).map(lambda x: x[1].dot(clusterCenters[x[0]])).sum())
    print(k, n-np.mean(nul_score), np.std(nul_score))
    nul_score_mean.append(n-np.mean(nul_score))

dat_score_mean = []
for k in range(2, 50, 2):
    dat_score = []
    for j in range(10):
        DSJP_df2 = DSJP_df.drop("prediction")
        kmeans = KMeans(k=k, featuresCol="vector_tf_idf_L2", seed=random.randint(1,1000000))#, seed=1)                                                                         
        model = kmeans.fit(DSJP_df2)
        DSJP_df2 = model.transform(DSJP_df2)
        clusterCenters = model.clusterCenters()
        dat_score.append(DSJP_df2.select("prediction").rdd.flatMap(lambda x: x).\
                         zip(DSJP_df.select("vector_tf_idf_L2").rdd.flatMap(lambda x: x)).map(lambda x: x[1].dot(clusterCenters[x[0]])).sum())
    print(k, n-np.mean(dat_score), np.std(dat_score))
    dat_score_mean.append(n-np.mean(dat_score))
```
</details>



## ML Production Readiness

As discussed in [this paper](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45742.pdf),
"Using machine learning in real-world production systems is complicated by a
host of issues not found in small toy examples or even large offline research
experiments. Testing and monitoring are key considerations for assessing the
production-readiness of an ML system."
The following prototype provides an *ML Test Score Rubric*  based on a set of actionable tests to
help quantify ML pipeline production readiness and
give an indication of how much testing and monitoring is enough.
Click on the plot or [this link](http://ec2-3-85-212-72.compute-1.amazonaws.com/#production_readiness) to explore the live interactive version
of the plot.

<p align="center">
<a href="http://ec2-3-85-212-72.compute-1.amazonaws.com/#production_readiness"><img src="images/prodready.jpeg"/></a>
</p>


## Bayes with *PyMC3*

My most recent project was to use *PyMC3*
to create a Bayesian trivariate regression inference analysis.
This model allows the dependency structure in the three outcome variables to be
directly modeled and characterized as a single joint variable, as opposed to
being assessed in an *ad hoc* marginal manner. 
The benefits of this approach are that it provides
1. **any desired quality metric** based on the joint outcome
2. **outcome comparison** accounting for internal dependency within the joint outcome
3. **ranking** to separate good subjects from bad subjects
4. **dependency estimation** for inference on internal outcome associations
5. **proper and complete uncertainty quantifications** on which to based sound conclusions

The model specification and example inference are given below
and a summary of the analysis is given [in this paper](schwartz-pyMC3-trigression.pdf).

<p align="center">
<a href="schwartz-pyMC3-trigression.pdf"><img src="images/bayes1.jpeg"/></a>
</p>
<p align="center">
<a href="schwartz-pyMC3-trigression.pdf"><img src="images/bayes2.jpeg"/></a>
</p>






## Afterward: p-values

*P-values* are a measure of evidence against a null hypothesis defined as

*"the probability of seeing something as or more extreme than what you saw if the null hypothesis were true."*

Operationally, p-values can be compared against the significance level of the test to determine the
rejection status of the null hypothesis, but further interpretation of p-values requires caution:

1. p-values do not characterize "the probability the null hypothesis is true"

   The mistake here is that in a technical sense this statement is nonsensical.
The truthfulness of a null hypothesis is not a random variable with a probability distribution
as the above sentiment implies; therefore, the association of the p-value as a meaningful quantification
of the desired sentiment is necessarily egregious. This pitfall clarifies that when interpreting p-values
one must not stray from the relevant definition.

2. p-values do not characterize "the probability the null hypothesis was incorrectly rejected"

   This is rather the significance level of the hypothesis test.  While the null hypothesis is not
conceptualized as a random variable, the decision to reject the null hypothesis
(and the mechanism by which this is done, e.g., comparing the p-value to the significance level)
is.  And further, the chance of error in decision is explicitly specified (under the assumptions of the test).
But this is the significance level, not the p-value, of the test.

3. p-values are not asymptotic probabilities of randomly sampled null hypotheses truthfulness

   If we actually do imagine we are sampling and testing some proportion of true and false null hypotheses,
it is still not true that the proportion of null hypotheses that are true at a given p-value level is
the p-value; rather, as is quickly seen via some simulation experiments, the p-value does not
have an direct correlation with the proportion of null hypotheses that are true at a given p-value level.


The following simulation dashboard shows the correlation of p-value and null hypotheses truthfulness
by plotting the proportion of true null hypotheses rejected at a given p-value level under various settings. 
Click on the plot or [this link](http://ec2-3-85-212-72.compute-1.amazonaws.com/#p_values) to explore the live interactive version
of the plot.

<p align="center">
<a href="http://ec2-3-85-212-72.compute-1.amazonaws.com/#p_values"><img src="images/pvals.jpeg"/></a>
</p>
