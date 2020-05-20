from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


class subsetDataFrame(BaseEstimator, TransformerMixin):
    """subset a pd.DataFrame to a given list of columns"""

    def __init__(self, target_columns):
        """
            target_columns (list) : names of columns which will be kept  
                                    upon subsetting with the transform method
        """
        
        self.target_columns = target_columns
        self.used_columns = None

    def fit(self, X, Y=None):
        """
            X (pd.DataFrame) : a pandas data frame to be subsetted
            Y (None) : not to be used -- not required
            
            SIDE EFFECT: makes sure columns named are actually available
                         and creates a list of columns to use which are
        """ 
        
        X_columns = X.columns.tolist()
        self.used_columns = [c for c in self.target_columns if c in X_columns]
        
        return self        
                
    def transform(self, X):
        """
            X (pd.DataFrame) : a pandas data frame to be subsetted
            
            RETURNS a subset of X as determined by initialized self.columns
        """
        
        return X[self.target_columns]
    


class oneHotEncoder(BaseEstimator, TransformerMixin):
    """One hot (re)encode categorical columns in a pd.DataFrame"""

    def __init__(self, target_columns):
        """
            target_columns (list) : names of (categorical type) columns which 
                                    will be replaced with one hot encoding by
                                    the transform method
        """
        
        self.target_columns = target_columns
        self.used_columns = None
        self.OHE_level_structure = None        
        
    def fit(self, X, Y=None):
        """
            X (pd.DataFrame) : a pandas data frame with categoricals
                               whose one hot encoding levels will be
                               identified (with missingness assigned 
                               to level ":nan")
            Y (None) : not to be used -- not required
            
            SIDE EFFECT : learns categorical levels present in X;
                          when transform is subsequently used it
                          produces one hot encoding conforming to
                          what was present in X during initial fit
                          
                          *Novel levels encountered during later
                          transform calls are set to level ":nan"
        """
        
        X_columns = X.columns.tolist()
        self.used_columns = [c for c in self.target_columns if c in X_columns]        
        X = X[self.used_columns]
        # ensure we get an '_na' level for every column
        X = X.append(pd.DataFrame(columns=X.columns, index=[-1]))
        # ensure column prefix delineator is not included in level
        # (so we can extract the level values later as needed)
        X.replace(':',';', inplace=True)
        
        tf_X = pd.get_dummies(X.apply(lambda x: x.astype('category')),
                              dummy_na=True, prefix_sep=':')
        self.OHE_level_structure = tf_X.columns.tolist()

        return self

    def transform(self, X):
        """
            X (pd.DataFrame) : a pandas data frame with categoricals
                               whose one hot encoding levels will be
                               identified (with missingness assigned 
                               to level ":nan")
                               
                               *must be a "similar enough" X to that 
                               initially passed to the fit method:
                               e.g., passing the same exact X column
                               structure, for example
            
            RETURNS a subset of X as determined by initialized self.columns
        """

        X_columns_ignored = [c for c in X.columns if c not in self.used_columns]
        tmp_X = X[self.used_columns].copy()
        # ensure column prefix delineator is not included in level
        # (so we can extract the level values later as needed)
        tmp_X.replace(':',';', inplace=True)
        tmp_X = pd.get_dummies(tmp_X.apply(lambda x: x.astype('category')),
                               dummy_na=True, prefix_sep=':')
        
        tf_X = pd.DataFrame(np.zeros((X.shape[0],len(self.OHE_level_structure))),
                            columns=self.OHE_level_structure, index=X.index)
        
        for c in tmp_X:
            if c in self.OHE_level_structure:
                tf_X[c] = tmp_X[c]|tf_X[c]
            else:
                c_na = ':'.join(c.split(':')[:-1])+':nan'
                tf_X[c_na] = tmp_X[c]|tf_X[c_na]
        
        return X[X_columns_ignored].join(tf_X.apply(lambda x: x.astype('int')))
    
class addMissingnessIndicators(BaseEstimator, TransformerMixin):
    """add columns tracking missingness in other columns"""

    def __init__(self, target_columns):
        """
            target_columns (list) : column names for which new missingness  
                                    indicator columns will be made
        """
        
        self.target_columns = target_columns
        self.used_columns = None

    def fit(self, X, Y=None):
        """
            X (pd.DataFrame) : a pandas data frame on which to append
                               indicator variables tracking missingness
                               of the columns specified in initialized 
                               self.columns, where possible (i.e., present)
            Y (None) : not to be used -- not required
            
            SIDE EFFECT: makes sure columns named are actually available
                         and creates a list of columns to use which are
        """ 
        
        X_columns = X.columns.tolist()
        self.used_columns = [c for c in self.target_columns if c in X_columns]
        
        return self        

    def transform(self, X):
        """
            X (pd.DataFrame) : a pandas data frame on which to append
                               indicator variables tracking missingness
                               of the columns specified in initialized 
                               self.columns, where possible (i.e., present)
                               
                               *must be a "similar enough" X to that 
                               initially passed to the fit method:
                               e.g., passing the same exact X column
                               structure, for example
            
            RETURNS an expanded pandas data frame with new columns
            tracking the missingness of other columns as determined 
            by initialized self.columns
        """
                
        X_columns = X.columns.tolist()
        X_columns_ignored = [c for c in X.columns if c not in self.used_columns]
        tmp_X = X[self.used_columns].copy()
        
        tf_X = np.zeros((tmp_X.shape[0], tmp_X.shape[1]*2), dtype="object")
        tf_X[:,:tmp_X.shape[1]] = tmp_X.values
        tf_X[:,tmp_X.shape[1]:] = tmp_X.isna().apply(lambda x: x.astype('int')).values
        tf_X = pd.DataFrame(tf_X, index=X.index,
                            columns=self.used_columns+\
                                    [c+":nan" for c in self.used_columns])
        
        return X[X_columns_ignored].join(tf_X)


class makeMissingnessMedian(BaseEstimator, TransformerMixin):
    """super simple"""

    def __init__(self):    
        self.medians = None
    
    def fit(self, X, Y=None):
        self.medians = X.median()
        return self

    def transform(self, X):
        """X needs to be the same structure as used in fit"""
        return X.fillna(self.medians)

    
class thresholdedRF(RandomForestClassifier):
    """
        This class exists to allow the .predict() method
        to predict at rates based on class (im)balance
    """

    def __init__(self, positive_class_rate=.5,
                       min_samples_leaf = 1,
                       n_estimators=100, max_features='auto'):
        """
            Must be passed 'positive_class_rate'
            which is stored as self.threshold
            
            All RandomForestClassifier parameters
            will be passed to that initialization
        """
        self.positive_class_rate = positive_class_rate
        super(thresholdedRF, self).__init__(max_features=max_features,
                                            min_samples_leaf=min_samples_leaf,
                                            n_estimators=n_estimators)
    
    def predict(self, X):    
        """
            Predictions are now made based on self.threshold
            which when set at class balance will try to make
            yhat.sum() approximately equal to y.sum() rather
            than just using the basic 0.5 threshold which
            does not take into account class balance
        """
        return self.predict_proba(X)[:,1] > self.positive_class_rate

    def transform(self, X):
        """pass through function to get the final data"""
        
        return X
    
