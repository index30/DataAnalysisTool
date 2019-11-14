import pandas as pd
from pathlib import Path 
from sklearn.feature_selection import (mutual_info_regression, SelectKBest, 
                                       SelectPercentile, VarianceThreshold)

class Processing:
    def __init__(self, **params):
        self.origin_X_train = params["X_train"]
        self.origin_X_test = params["X_test"]
        self.result_X_train = params["X_train"]
        self.result_X_test = params["X_test"]
    
    def get_origin(self):
        return self.origin_X_train, self.origin_X_test
        
    def get_result(self):
        return self.result_X_train, self.result_X_test
    
    def put_log(self, add_txt):
        print(add_txt)
        print("Train columns {}".format(len(self.result_X_train.columns)))
        print("Test columns {}".format(len(self.result_X_test.columns)))
        
    def del_by_variance(self, threshold, verbose=0):
        if verbose:
            self.put_log("Origin featured")
        sel = VarianceThreshold(threshold=0.1)
        sel.fit(self.result_X_train)
        self.result_X_train = self.result_X_train.loc[:, sel.get_support()]
        self.result_X_test = self.result_X_test.loc[:, sel.get_support()]
        if verbose:
            self.put_log("Processed featured")
    
    def del_by_duplicate(self, verbose=0):
        if verbose:
            self.put_log("Origin featured")
        X_train_T = self.result_X_train.T
        print("Duplicated feature {}".format(X_train_T.duplicated().sum()))

        duplicated_features = X_train_T[X_train_T.duplicated()].index.values

        self.result_X_train = self.result_X_train.drop(duplicated_features, axis=1)
        self.result_X_test = self.result_X_test.drop(duplicated_features, axis=1)
        
        if verbose:
            self.put_log("Processed featured")
    
    def pickup_MI_features(self, y_train, choice=("percent", 10), verbose=0):
        if verbose:
            self.put_log("Origin featured")
        MI = mutual_info_regression(self.result_X_train, y_train)
        MI = pd.Series(MI)
        MI.index = self.result_X_train.columns
        MI.sort_values(ascending=False).plot(kind='bar', figsize=(20,10))

        # KBest : 抽出する特徴量の"数"を指定
        if not choice[0] == "percent":
            pick_sel = SelectKBest(mutual_info_regression, k=choice[1])
        else:
            pick_sel = SelectPercentile(mutual_info_regression, percentile=choice[1])
        pick_sel.fit(self.result_X_train, y_train)

        self.result_X_train = self.result_X_train.loc[:, pick_sel.get_support()]
        self.result_X_test = self.result_X_test.loc[:, pick_sel.get_support()]
        if verbose:
            self.put_log("Processed featured")


if __name__ == "__main__":
    p = Processing()