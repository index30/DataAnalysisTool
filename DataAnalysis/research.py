from pathlib import Path
import sys
import lightgbm as lgb
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import (RandomForestRegressor, AdaBoostRegressor, 
                              GradientBoostingRegressor, ExtraTreesRegressor)

import preprocessing, processing


class Research():
    def __init__(self):
        pass
    
    def lgb_model_params(self):
        lgb_params = {'num_leaves': [25, 50, 98],
                      'learning_rate': [0.01, 0.1, 1],
                      'n_estimators': [100, 200, 500],
                      'max_depth': [4, 6, 8, 10, 20, -1]}
        lgb_model = lgb.LGBMRegressor()
        return lgb_params, lgb_model
    
    def xgb_model_params(self):
        # xgb_params = {'learning_rate': [0.01, 0.1, 1],
        #               'n_estimators': [100, 200, 500],
        #               'max_depth': [4, 6, 8, 10, 20, -1]}
        xgb_params = {'learning_rate': [0.01, 0.1]}
        xgb_model = xgb.XGBRegressor()
        return xgb_params, xgb_model
    
    def rf_model_params(self):
        rf_params = {'n_jobs': [-1, 2, 4],
                     'n_estimators': [10, 50, 100],
                     'max_features': [0.1, 0.2, 0.5],
                     'max_depth': [4, 6, 8, 10, 20, None],
                     'min_samples_leaf': [2, 4]}
        rf_model = RandomForestRegressor()
        return rf_params, rf_model
    
    def et_model_params(self):
        et_params = {'n_jobs': [-1, 2, 4],
                     'n_estimators': [10, 50, 100],
                     'max_features': [0.1, 0.2, 0.5],
                     'max_depth': [4, 6, 8, 10, 20, None],
                     'min_samples_leaf': [2, 4]}
        et_model = ExtraTreesRegressor()
        return et_params, et_model
    
    def gb_model_params(self):
        gb_params = {'n_estimators': [10, 50, 100],
                     'max_features': [0.1, 0.2, 0.4],
                     'max_depth': [4, 6, 8, 10, 20, -1],
                     'min_samples_leaf': [2, 4]}
        gb_model = GradientBoostingRegressor()
        return gb_params, gb_model
    
    def grid_search(self, model, data, label, params, CV=5):
        gs = GridSearchCV(
            model,
            params,
            cv=CV
        )
        gs.fit(data, label)
        print(gs.best_score_)
        print(gs.best_params_)


if __name__=="__main__":
    argv = sys.argv[1:]
    mdl_type = argv[0]
    
    train_path = Path('../data/train.csv')
    test_path = Path("../data/test.csv")
    pp = preprocessing.Preprocessing()
    train_df = pp.load_data(train_path.as_posix())
    test_df = pp.load_data(test_path.as_posix())
    train_df = pp.cut_na(train_df)
    test_df = pp.cut_na(test_df)
    
    print("Finish loading Data")
    
    train_columns = train_df.columns.to_list()
    train_columns.remove("ID")
    test_columns = test_df.columns.to_list()
    test_columns.remove("ID")

    train_df = pp.load_feature_list(train_df, train_columns)
    test_df = pp.load_feature_list(test_df, test_columns)
    
    corr_columns = pp.pickup_corr_lists(train_df, "Score", 800)

    train_df, label_df = pp.split_Xy(train_df, "Score")
    train_int_df = pp.val2int(train_df)
    
    res = Research()
    print("Initialized research")
    
    if mdl_type == "lgb":
        print("Use lgb")
        params, model = res.lgb_model_params()
    else:
        print("Use xgb")
        params, model = res.xgb_model_params()
    
    res.grid_search(model, train_int_df, label_df, params)