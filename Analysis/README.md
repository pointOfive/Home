# Data Analysis

## Data Pipelining Functionality

The `Scikit-Learn` `Pipeline` package
facilitates data processing and transformation within a cross validation
context by providing `pipeline` objects that envoke a series of `.transform`
methods as part of `.fit` and `.predict` calls. 
This functionality simplifies and abstracts the
data modeling process, but the capabilities available out of the box
leave some things to be desired; namely, the built-in `Transforer` objects
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
                tmp = X[:,np.array(self.colnames) == self.to_be_transformed[c1]]*X[:,np.array(self.colnames) == self.to_be_transformed[c2]]
                if np.std(tmp) != 0.0:
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
        Xdat = pd.DataFrame(Xdat,columns=self.colnames)
        Xdat = add_constant(Xdat)
        for c in self.drop:
            del Xdat[c]
        self.model = Logit(Ydat, Xdat)
        self.results = self.model.fit_regularized(method='l1', alpha=np.array([0]+[self.alpha]*(Xdat.shape[1]-1)),trim_mode='off')#fit()
        return self

    def predict(self, Xdat=None):
        if Xdat is None:
            return self.results.predict()
        else:
            Xdat = pd.DataFrame(Xdat,columns=self.colnames)
            Xdat = add_constant(Xdat)
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
        Xdat = add_constant(Xdat)            
        self.model = OLS(Ydat, Xdat, hasconst=True)
        self.results = self.model.fit()
        return self

    def predict(self, Xdat=None):
        if Xdat is None:
            return self.results.predict()
        else:
            Xdat = pd.DataFrame(Xdat,columns=self.colnames)
            Xdat = add_constant(Xdat)
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


## Statistical Analysis

The final two custom data pipelining functionalities 
concern themselves with "classical" exercises specific to `Linear Model` operationalization, 
but they allow us to carry desirable statistical analysis capabilities forward into
the modern supervised learning framework. The following example demonstrates the
synergistic integration of regularization and uncertainty quantification
in the context of multiplicative association identificaiton in classification settings.
Please visit [this AWS server](www.google.com) to explore the live interactable version
of this plot. 

[PUT A LINKABLE SCREENSHOT HERE]

Methodoloigies such as `Random Forests`,
`Support Vector Machines` (via the `Kernel Trick`), and `Gradient Boosted Trees`
automatically leverage extremely complex higher order interaction associations, but
any higher order interaction associations to be considered in the context of
`Linear Models` require explicit *a priori* specification and construction.
As a result, `Linear Model` specifications cannot realistically consistently compete with
the modeling flexibility provided by modern predictive machine learning methodologies; however, 
the statistical analysis capabilities available
within a `Linear Model` framework serve to ensure
it's competetiveness as an analytical tool by
providing uncertainty characterizations
that can be brought to bear on questions of model building and interpretation.


## Model Interpretation and Use

### Machine Learning is no more "black box" than a Linear Model

As noted above, the benefit of `Linear Model` frameworks is
the uncertainty characterizations they provide. 
On the contrary, the frequent charge that a benefit of `Linear Model` frameworks over 
modern machine learning predictive methodologies is that the latter
only provides black box tools lacking interpretation capabilities is patently incorrect.

- the commendable *"hold all but one feature constant"* standard `Linear Model` interpretaion
is available in all contexts as a so-called *Partial Dependency Plot*
- examinations of the presence of specific interactions requires their explicit construction,
and can be carried out on the basis of *Feature Importance Diagnostics* -- not only via hypothesis testing

The following example demonstrates partial dependency plots and feature importance diagnostics.
Please visit [this AWS server](www.google.com) to explore the live interactable version
of this plot.

### Experimental design (still) drives interpretability

The real issue in interpreting feature-outcome associations comes down to experiemental design;
specifically, it is feature correlation which limits association attribution and the ever present
risk of actual confounding that renders associations non causitive.



Interpretation of "feature effect" in all models therefore comes down to questions of
experiemental design; namely, intentional sampling across features can produce uncorrelated
features and hence unconfounded association interpretation.

When assessing intepretability, feature correlation, and

An attractive approach to
correlated features is [principal components regression, as demonstrated here](www.google.com).

### Model Based Decision Making

Model use execution... cost-benefit decision making

Please visit this [Bokeh Server](www.google.com) to interact with this plot.



## Model Tuning Parameter Selection

Modern predictive methodology avoids overfitting 
by using cross validation techniques to identify appropriate regularization levels.
The `Kfolds` and `GridSearchCV` functionalities in `Scikit-Learn` greatly
facilitate and simplify this task.  


Random Forests provide near cutting edge prediction out of the box
with very little parameter tuning. This is because (to the extent possible)
Random Forests grossly overfit to the training data, but conflate
intrinsic error with model error, so that 

<details>
<summary>
K-folds Cross Validation for Random Forests
</summary>

<br>


</details>


These capabilities are demonstrated below,
as well as a custom grid search for XGboost that returns the optimal model
based on postprocessing of out of sample scoring during the
sequential ensemble f



## Afterward: p-values

*P-values* are a measure of evidence against a null hypothesis defind as

*"the probability of seeing something as or more extreme than what you saw if the null hypothesis were true"*

Operationally, p-values can be compared against the significance level of the test to determine the
rejection status of the null hypothesis, but further interpretation of p-values requires caution:

1. p-values do not characterize "the probability the null hypothesis is true"

The mistake here is that in a technical sense this statement is nonsensical.
The truthfulness of a null hypothesis is not a random variable with a probability distribution
as the above sentiment implies; therefore, the association of the p-value as a meaningful quantification
of the desired sentiment is necessarily aggregious. This pitfall clarifies that when interpreting p-values
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
the p-value; rather, as is quickly seen via some simulation experiements, the p-value does not
have an direct correlation with the proportion of null hypotheses that are true at a given p-value level.

The following interactive dashboard shows the correlation of p-value and null hypotheses truthfulness
by plotting the proportion of true null hypotheses rejected at a given p-value level.
The relevant setting are:

- proportion of null hypotheses that are false (which is user defined input)
- the distribution of effect sizes under the alternative hypotheses (which is taken to be uniformly random)


