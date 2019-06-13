import pandas as pd
from pathlib import Path

class Preprocessing:
    def __init__(self):
        pass

    def load_data(self, data_path, header=0):
        data_path = Path(data_path)
        if data_path.suffix == ".csv":
            df = pd.read_csv(data_path.as_posix(), header=header)
        elif data_path.suffix == ".xlsx":
            df = pd.read_excel(data_path.as_posix(), header=header)
        else:
            df = pd.read_table(data_path.as_posix(), header=header)
        return df

if __name__ == "__main__":
    pp = Preprocessing()