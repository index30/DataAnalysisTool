import numpy as np
import pandas as pd
from pathlib import Path

class Preprocessing:
    def __init__(self):
        pass

    # Load from data file
    def load_data(self, data_path, header=0):
        data_path = Path(data_path)
        if data_path.suffix == ".csv":
            df = pd.read_csv(data_path.as_posix(), header=header)
        elif data_path.suffix == ".xlsx":
            df = pd.read_excel(data_path.as_posix(), header=header)
        else:
            df = pd.read_table(data_path.as_posix(), header=header)
        return df

    # Select from dataframe    
    def load_feature_list(self, df, features):
        return df.loc[:, features]
    
    # The process of cutting NA
    # 欠損値の処理
    def cut_na(self, df, option=None):
        if option=="mean":
            # Fill na to mean
            return df.fillna(df.mean().mean(), axis=0)
        return df.fillna(0, axis=0)
    
    # Split X and y from dataframe
    # 特定のカラムを正解ラベルとして、学習データと正解データとして返す
    def split_Xy(self, df, y_name):
        
        df_copy = df.copy()
        y = df_copy[y_name]
        X = df_copy.drop(y_name, axis=1)
        return X, y
    
    # corr_nameで指定したカラムでデータ全体に対してとった相関の
    # 上位corr_top分のカラムを返却する
    def pickup_corr_lists(self, df, corr_name, corr_top=50):
        corr_df = df.corr()
        top_corr_df = corr_df[corr_name].sort_values(ascending=False)[1:]
        top_corr_col = top_corr_df.keys()[:corr_top]
        return top_corr_col
    
    # intとfloatを区別
    def devide_intfloat(self, df):
        df_columns = df.columns
        int_list = [df[x].dtype == np.int64 for x in df_columns]
        float_list = [df[x].dtype == np.float64 for x in df_columns]
        return int_list, float_list
    
    # カラムが2値かどうかを区別
    def devide_binary(self, df):
        target_columns = df.columns
        binary_list = [len(df[x].unique()) == 2 for x in target_columns]
        not_binary_list = [len(df[x].unique()) != 2 for x in target_columns]
        return binary_list, not_binary_list
        
    
    def val2int(self, df):
        df = df.astype(np.int64)
        return df

if __name__ == "__main__":
    pp = Preprocessing()