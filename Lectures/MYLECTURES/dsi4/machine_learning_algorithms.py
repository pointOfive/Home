'''
CHEAT SHEET FOR DIFFERENT REGRESSION, CLASSIFICATION, NLP  AND UNSUPERVISED ALGORITHMS
'''

'''GENERAL IMPORTS'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''PREPARING DATA/CLEANING DATAFRAME'''
df = pd.read_csv('file_name.csv') ##read in csv file

df = df.drop([col1, col2, col3],axis=1) ##drop unnecessary columns
b_loon = {'no':0, 'yes':1}
for col in [col1, col2]:
    df[col] = df[col].map(b_loon)
##goes through list of column names with no/yes values (col1, col2) and replaces
##yes/no with 1/0
y_data = df.pop(y_column_name).values
X_data = df.values

'''TEST/TRAIN SPLITTING'''
try:
    from sklearn.model_selection import train_test_split
except:
    from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X , y, test_size=0.25)

'''CROSS-VALIDATION'''
try:
    from sklearn.model_selection import cross_val_score
except:
    from sklearn.cross_validation import cross_val_score
##define the regression/classification model first and then pass into...
cross_val_score(model, X_train, y_train, scoring='mean_squared_error', cv=5)

#possible options for scoring: ['accuracy', 'adjusted_rand_score',
# 'average_precision', 'log_loss', 'mean_absolute_error', 'mean_squared_error',
# 'precision', 'precision_macro', 'precision_micro', 'precision_samples',
#'precision_weighted', 'r2', 'recall', 'recall_macro', 'recall_micro', 'recall_samples',
# 'recall_weighted', 'roc_auc']

#cv is the number of splits for cross validation

'''SCORING TEST DATA'''
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_true, y_predicted)

##other scoring modules that can be imported from sklearn.metrics:
##Classification: [accuracy_score, precision_score, roc_curve, log_loss]
##Regression: [r2_score, mean_absolute error, mean_squared_error]


'''NORMALIZING DATA'''
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

'''SELECTING IMPORTANT FEATURES'''
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

feat = SelectKBest(score_func=chi2, k=8)
## k is number of features to be selected
##score_func: f_classif and chi2 for classification, f_regression for regression
feat.fit(X_data,y_data)
X_new = feat.transform(X_data)
##returns X_new which only has the k=8 most important features
features = feat.get_support(indices=True)
##returns indices of features selected


'''PARAMETER TUNING'''
from sklearn.grid_search import GridSearchCV
param_grid = {'par1': [list1],
              'par2': [list2]}      ##parameters to be tuned and list to choose from

##define the regression/classification model first and then pass into...
best_model = GridSearchCV(model, param_grid, n_jobs=-1, scoring='accuracy',
                        cv=10).fit(X_train, y_train)

bestmodel.best_params_          ##parameters used to get best fit
bestmodel.best_score_          ##score after tuning
bestmodel.best_estimator_       #new model with tuned parameters


'''LINEAR REGRESSION (for regression)'''
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True, normalize=False)
model.fit(X_train, y_train)
model.predict(X_test)
model.score(X_test, y_test)     ##retuns R^2


'''LOGISTIC REGRESSION (for classification)'''
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(C=1.0, fit_intercept=True, intercept_scaling=1)
##C: Inverse of regularization strength; must be a positive float.
##To lessen the effect of regularization on synthetic feature weight
##(and therefore on the intercept), intercept_scaling has to be increased.

model.fit(X_train, y_train)
probabilities = model.predict_proba(X_test)
##Returns the probability of the sample for each class in the model
prediciton = model.predict(X_test)
#Predict class labels for samples in X_test
model.score(X_test, y_test)     ##returns mean accuracy


'''LINEAR REGRESSION WITH REGULARIZATION'''
from sklearn.linear_model import Ridge
model = Ridge(alpha=1, fit_intercept=True, normalize=False)
model.fit(X_train, y_train)
model.predict(X_test)
model.score(X_test, y_test)     ##retuns R^2

from sklearn.linear_model import Lasso
model = Lasso(alpha=1, fit_intercept=True, normalize=False)
model.fit(X_train, y_train)
model.predict(X_test)
model.score(X_test, y_test)     ##retuns R^2


'''K NEAREST NEIGHBORS (Regression and classification)'''
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5, p=2)
##p=1: manhattan_distance; p=2: euclidean_distance
model.fit(X_train, y_train)
probabilities = model.predict_proba(X_test)
prediction = model.predict(X_test)
model.score(X_test, y_test)     ##returns mean accuracy

from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor(n_neighbors=5, p=2)
model.fit(X_train, y_train)
prediction = model.predict(X_test)
model.score(X_test, y_test)     ##returns R^2


'''DECISION TREES (Regression and classification)'''
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None)
##criterion is either 'gini' or 'entropy' - the function to measure the quality of split
model.fit(X_train, y_train)
model.predict(X_test)
model.predict_proba(X_test)
model.predict_log_proba(X_test)
model.score(X_test, y_test)     ##returns mean accuracy

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(criterion='mse', splitter='best', max_depth=None)
##criterion is either 'mse' or 'mae' - the function to measure the quality of split
model.fit(X_train, y_train)
model.predict(X_test)
model.score(X_test, y_test)     ##returns R^2


'''BAGGING (Regression and classification)'''
from sklearn.ensemble import BaggingClassifier
model = BaggingClassifier(n_estimators=10, max_samples=1.0)
##n_estimators: The number of trees in the ensemble.
##max_samples: The number of samples to draw from X to train each base estimator.
model.fit(X_train, y_train)
model.predict(X_test)
model.predict_proba(X_test)
model.predict_log_proba(X_test)
model.score(X_test, y_test)     ##returns mean accuracy

from sklearn.ensemble import BaggingRegressor
model = BaggingRegressor(n_estimators=10, max_samples=1.0)
model.fit(X_train, y_train)
model.predict(X_test)
model.score(X_test, y_test)     ##returns R^2


'''RANDOM FOREST (Regression and classification)'''
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=10, max_depth=None, max_features='auto')
##n_estimators: The number of trees in the ensemble.
##max_samples: The number of samples to draw from X to train each base estimator.
model.fit(X_train, y_train)
model.predict(X_test)
model.predict_proba(X_test)
model.predict_log_proba(X_test)
model.score(X_test, y_test)     ##returns mean accuracy

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=10, max_depth=None, max_features='auto')
model.fit(X_train, y_train)
model.predict(X_test)
model.score(X_test, y_test)     ##returns R^2


'''GRADIENT BOOSTING (Regression and classification)'''
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(n_estimators=10, learning_rate=0.1, max_depth=None, max_features='auto')
model.fit(X_train, y_train)
model.predict(X_test)
model.predict_proba(X_test)
model.predict_log_proba(X_test)
model.score(X_test, y_test)     ##returns mean accuracy

from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor(n_estimators=10, learning_rate=0.1, max_depth=None, max_features='auto')
model.fit(X_train, y_train)
model.predict(X_test)
model.score(X_test, y_test)     ##returns R^2


'''ADABOOST (Regression and classification)'''
from sklearn.ensemble import AdaBoostClassifier
model = AdaBoostClassifier(n_estimators=50, learning_rate=1.0)
model.fit(X_train, y_train)
model.predict(X_test)
model.predict_proba(X_test)
model.predict_log_proba(X_test)
model.score(X_test, y_test)

from sklearn.ensemble import AdaBoostRegressor
model = AdaBoostRegressor(n_estimators=50, learning_rate=1.0)
model.fit(X_train, y_train)
model.predict(X_test)
model.score(X_test, y_test)

'''XGBOOST (Regression and classification)'''
#pip install xgboost
## able to handle data with missing values and NaNs
from xgboost import XGBClassifier
model = XGBClassifier()
##parameters: max_depth=3, learning_rate=0.1, n_estimators=100, silent=True,
##objective='reg:linear', booster='gbtree', n_jobs=1, nthread=None, gamma=0,
##min_child_weight=1, max_delta_step=0, subsample=1, colsample_bytree=1,
##colsample_bylevel=1, reg_alpha=0, reg_lambda=1, scale_pos_weight=1,
##base_score=0.5, random_state=0, seed=None, missing=None
model.fit(X_train, y_train)
model.predict(X_test)
model.predict_proba(X_test)
model.predict_log_proba(X_test)
model.score(X_test, y_test)

from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_train, y_train)
model.predict(X_test)
model.score(X_test, y_test)


'''SUPPORT VECTOR MACHINES (Classification and Regression, better suited for classification)'''
from sklearn.svm import SVC
model = SVC(C=1.0, degree=3, gamma='auto', kernel='linear')
##Penalty parameter C of the error term for regularization
##kernel is either 'linear', 'rbf', or 'poly'
##degree represents the degree of polynomial kernel
##gamma is the parameter for rbf kernel
model.fit(X_train,y_train)
model.predict(X_test)
model.score(X_test, y_test)

from sklearn.svm import SVR
model = SVR(C=1.0, degree=3, gamma='auto', kernel='linear')
model.fit(X_train,y_train)
model.predict(X_test)
model.score(X_test, y_test)

'''DEALING WITH MULTIPLE CLASSES IN y_train'''
from sklearn.multiclass import OneVsOneClassifier
##define the regression/classification model first and then pass into...
model_multiclass = OneVsOneClassifier(model, n_jobs=-1)
model_multiclass.fit(X_train,y_train)
predictions = model_multiclass.predict(X_test)

from sklearn.multiclass import OneVsRestClassifier
##define the regression/classification model first and then pass into...
model_multiclass = OneVsRestClassifier(model, n_jobs=-1)
model_multiclass.fit(X_train,y_train)
predictions = model_multiclass.predict(X_test)


'''NATURAL LANGUGAE PROCESSING WITH MULTINOMIAL NAIVE BAYES'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from nltk.corpus import stopwords
import string
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
porter = PorterStemmer()
snowball = SnowballStemmer('english')
wordnet = WordNetLemmatizer()
import copy
def tokenize(doc):
    '''
    INPUT: string
    OUTPUT: list of strings

    Tokenize and stem/lemmatize the document.
    '''
    tokenized_doc = nltk.word_tokenize(doc)
    sw = set(stopwords.words('english'))

    toc_doc = []
    for token in tokenized_doc:
        if token not in sw:
            toc_doc.append(token)
    tokenized_doc = toc_doc
    sp = set(string.punctuation)
    sp.add('``')
    sp.add("''")

    toc_doc = []
    for token in tokenized_doc:
        if token not in sp:
            toc_doc.append(token)
    tokenized_doc = toc_doc

    tokenized_doc_porter = copy.deepcopy(tokenized_doc)
    for token in range(len(tokenized_doc)):
        tokenized_doc_porter[token] = porter.stem(tokenized_doc[token])
    return tokenized_doc_porter

vectorizer = TfidfVectorizer(tokenizer=tokenize)
vectorizer.fit(X_train)
X_tfidf = vectorizer.transform(X_train)
model = MultinomialNB()
model.fit(X_tfidf, y_train)
predictions = model.predict(vectorizer.transform(X_test))
probabilities = model.predict_proba(vectorizer.transform(X_test))
score = model.score(vectorizer.transform(X_test), y_test)

##cosine similarities
from sklearn.metrics.pairwise import linear_kernel
cos_sims = linear_kernel(X_tfidf, X_tfidf)


'''NEURAL NETWORKS (Classification)'''
keras doc: https://keras.io/getting-started/sequential-model-guide/#examples
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation,MaxPooling2D, Conv2D
from keras.optimizers import SGD
from sklearn.preprocessing import StandardScaler

model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Dense(64, activation='relu', input_dim=20))
#input_dim = X_data.shape[1]
model.add(Dropout(0.05))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.05))
model.add(Dense(10, activation='softmax'))
#10 in last layer is number of target classes, 1 if binary

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
#sgd is stochastic gradient descent; lr is learning rate
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
#activation functions include: 'relu', 'softmax', 'sigmoid'
#loss functions include: 'binary_crossentropy',  'categorical_crossentropy', 'mean_squared_error'

model.fit(x_train, y_train, epochs=20, batch_size=128)
predictions = model.predict(X_test, batch_size=128)
score = model.evaluate(X_test, y_test, batch_size=128)


'''CLUSTERING (UNSUPERVISED)'''
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters)
kmeans.fit(X_data)
prediction = kmeans.predict(X_new) ## predcits what cluster X belongs to
kmeans.labels_      ## after fitting, this will give cluster number/label of each point in X_data

for i in xrange(n_clusters):
    ##code snippet to get most important words in each cluster
    ##vect = TfidfVectorizer()
    index = np.argsort(kmeans.cluster_centers_[i])[::-1][:10]
    feature = np.array(vect.get_feature_names())[index]
    print "Cluster", i, feature


'''DIMENSIONALITY REDUCTION (PCA)'''
from sklearn.decomposition import PCA
pca = PCA(n_components=10)      ##n_components is number of components to reduce X to
pca.fit(X_data_scaled)          ## scale data before fitting
X_transform = pca.transform(X_data_scaled)      ##ready to be input into ML model


'''RECOMMENDATION SYSTEMS (NMF, SVD, KNNBasic)'''
# http://surprise.readthedocs.io/en/latest/evaluate.html
# pip install scikit-surprise
from surprise.prediction_algorithms.matrix_factorization import SVD
## other algorothms include surprise.prediction_algorithms.
## knns.KNNBasic, knns.KNNBasicWIthMeans, matrix_factorization.NMF, matrix_factorization.SVDpp
from surprise import Dataset
from surprise.dataset import Reader
from surprise import evaluate, print_perf

file_path = os.path.expanduser('recommendation-systems-files/data/u.data')
reader = Reader(line_format='user item rating timestamp',sep='\t')

# With data splitting
data = Dataset.load_from_file(file_path, reader=reader)
data.split(n_folds=5)
algo = SVD(reg_all=0.05)
perf = evaluate(algo, data_split, measures=['RMSE', 'MAE'])
## evaluate performance of algorithm by cross validaation on n_folds
print_perf(perf)
algo.train(algo.trainset)
prediction = algo.predict(uid='1',iid='50')[3]

#with full dataset
data = Dataset.load_from_file(file_path, reader=reader)
trainset = data.build_full_trainset()
algo = SVD(reg_all=0.05)
algo.train(trainset)
prediction = algo.predict(uid='1',iid='50')[3]


'''WEB SCRAPING BASICS'''
import requests
from bs4 import BeautifulSoup

url = url
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
search_count = soup.find('div', id='searchCount')
search_count = soup.select('selector')


'''GRAPH THEORY (WITH NETWORKX)'''
import networkx as nx
G = nx.read_edgelist(edge_filename, delimiter='\t')
G.number_of_edges()     ## gives number of edges
G.number_of_nodes()     ## gives number of nodes
nx.shortest_path(G, source=source, target=target)   ## gives shortest path between source and target

Counter(nx.degree_centrality(G)).most_common(10)
Counter(nx.betweenness_centrality(G)).most_common(10)
Counter(nx.eigenvector_centrality(G)).most_common(10)
## Gives list of top 10 most central based on each centrality measure

'''FINDING COMMUNITIES IN GRAPH THEORY'''
def girvan_newman_step(G):
    '''
    INPUT: Graph G
    OUTPUT: None

    Run one step of the Girvan-Newman community detection algorithm.
    Afterwards, the graph will have one more connected component.
    '''
    original_cc = len(list(nx.connected_components(G)))
    eb = dict()
    new_cc = len(list(nx.connected_components(G)))

    while new_cc == original_cc:
        ebbig = Counter(nx.edge_betweenness_centrality(G)).most_common(1)[0][0]
        G.remove_edge(ebbig[0], ebbig[1])
        new_cc = len(list(nx.connected_components(G)))

def find_communities_n(G, n):
    '''
    INPUT: Graph G, int n
    OUTPUT: list of lists

    Run the Girvan-Newman algorithm on G for n steps. Return the resulting
    communities.
    '''
    G1 = G.copy()
    for i in xrange(n):
        girvan_newman_step(G1)
    return list(nx.connected_components(G1))


def find_communities_modularity(G, max_iter=None):
    '''
    INPUT:
        G: networkx Graph
        max_iter: (optional) if given, maximum number of iterations
    OUTPUT: list of lists of strings (node names)

    Run the Girvan-Newman algorithm on G and find the communities with the
    maximum modularity.
    '''
    degrees = G.degree()
    num_edges = G.number_of_edges()
    G1 = G.copy()
    best_modularity = -1.0
    best_comps = nx.connected_components(G1)
    i = 0
    while G1.number_of_edges() > 0:
        subgraphs = nx.connected_component_subgraphs(G1)
        modularity = get_modularity(subgraphs, degrees, num_edges)
        if modularity > best_modularity:
            best_modularity = modularity
            best_comps = list(nx.connected_components(G1))
        girvan_newman_step(G1)
        i += 1
        if max_iter and i >= max_iter:
            break
    return best_comps


def get_modularity(subgraphs, degrees, num_edges):
    '''
    INPUT:
        subgraphs: graph broken in subgraphs
        degrees: dictionary of degree values of original graph
        num_edges: float, number of edges in original graph
    OUTPUT: Float (modularity value, between -0.5 and 1)

    Return the value of the modularity for the graph G.
     '''
    m = num_edges
    d = degrees
    front_constant = 1.0 / (2 * m)
    outsum = []

    for subgraph in subgraphs:
        edges = subgraph.edges()
        A = 0
        insum = []

        for i in subgraph.nodes_iter():
            for j in subgraph.nodes_iter():
                if (i, j) in edges:
                    A = 1
                else:
                    A = 0
                insum.append(A - ((d[i] * d[j]) / (2.0 * m) ))

        outsum.append(sum(insum))

    return front_constant * sum(outsum)


'''HELPFUL NOTES'''
precision = TP/(TP+FP)
recall = TP/(TP+FN)
specificity = 1 - alpha = TN/(FP+TN)
beta = 1 - power = FN/(TP+FN)
false positive rate = FP/(FP+TN)
true Positive Rate = TP/(TP+FN)

In Lasso and Ridge lambda controls the impact of penalty term which has the
effect of influencing the overall magnitudes (ablsoulte sizes) of the
regression coefficients. By increasing lambda the coefficients are
forced to be smaller and hence have smaller impacts in linear model predictions.

In SVMs the penalty term is comprised of the total summation of margin violations
and the lambda paramater controls the impact of the these violations on the
optimization. Specifically, a smaller lambda tolerates more margin violations.
Thus, decreasing lambda increases model bias, but with the benefit of
reducing model variance.

Sampling density is proportional to N^(1/p) where N is the number of points and
p is the number of dimensions in the input space.
