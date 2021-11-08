import os.path

import pandas as pd
from connect import DATA_PATH
from typing import Dict, List


def put_stock_data(datafile, new_data):
    data_file_path = os.path.join(DATA_PATH, datafile)
    df = pd.read_csv(data_file_path)

    for row in new_data:
        if row[0] in list(df["Date"]):
            print("Existing data will be overwritten for date:", row[0])
            df[df["Date"] == row[0]] = row
        else:
            print("New data will be added for date:", row[0])
            df = df.append(pd.DataFrame([row], columns=list(df.columns)), ignore_index=True)

    df.to_csv(data_file_path, index=False)
    print("Date file", data_file_path, "has been updated.")


def put_deletion(datafile, date_keys_to_rm: List[str]):
    data_file_path = os.path.join(DATA_PATH, datafile)
    df = pd.read_csv(data_file_path)
    num_rows = df.shape[0]
    for key in date_keys_to_rm:
        df = df[df["Date"] != key]
    print(f"{num_rows - df.shape[0]} row(s) found for deletion.")
    confirm = input("Do you confirm to perform the deletion? (Y/n): ")
    if confirm == "Y":
        df.to_csv(data_file_path, index=False)
        print("Date file", data_file_path, "has been updated.")
    else:
        print("No operation performed")


if __name__ == "__main__":
    print("Test delete data")
    put_deletion("SBUX.csv", date_keys_to_rm=["01/12/2021"])

    print("\nTest create or update")
    new_data = [["01/08/2018",88,88,88,88,88,88], ["01/12/2021",888,888,888,888,888,888]]
    put_stock_data("SBUX.csv", new_data)

