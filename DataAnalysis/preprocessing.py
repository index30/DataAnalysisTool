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
    def cut_na(self, df):
        return df.fillna(0, axis=0)
    
    # Split X and y from dataframe
    def split_Xy(self, df, y_name):
        df_copy = df.copy()
        y = df_copy[y_name]
        X = df_copy.drop(y_name, axis=1)
        return X, y

if __name__ == "__main__":
    pp = Preprocessing()