import os.path

import pandas as pd
from connect import DATA_PATH
from datetime import datetime
from typing import List, Optional

def get_stock_data(datafile, colnames: Optional[List]=None, start="01/12/2016", end="01/11/2021"):
    df = pd.read_csv(os.path.join(DATA_PATH, datafile))

    if colnames == None:
        colnames = list(df.columns)

    df["dto"] = [datetime.strptime(x, "%d/%m/%Y") for x in df["Date"]]
    start_dto = datetime.strptime(start, "%d/%m/%Y")
    end_dto = datetime.strptime(end, "%d/%m/%Y")

    subset = df[(df["dto"] >= start_dto) & (df["dto"] <= end_dto)][colnames]

    return subset

if __name__ == "__main__":
    print(get_stock_data("SBUX.csv", start="01/02/2021"))

