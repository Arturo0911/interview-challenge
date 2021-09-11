#!/usr/bin/python

"""
@author Arturo Negreiros Samanez
This code base was creted to automatice fetch the current change
and store in database
"""


import pandas as pd
from datetime import datetime
import pandas_datareader as pdr
from pprint import pprint


def get_info(start_date: datetime, end_date: datetime, selection=None):
    # data = pdr.get_data_yahoo(symbols=selection, start=start_date, end=end_date)
    # data = pd.DataFrame(data["Adj Close"])

    try:
        eur = pdr.DataReader('EURUSD=X', 'yahoo', start=start_date, end=end_date)['Adj Close']

        parsed = pd.DataFrame(eur)
        print(parsed["Adj Close"].iloc[0:2][0])
        for x in parsed.to_numpy():
            print(x)
        # return parsed.to_numpy()
        # print(dir(eur))
        # print(eur[""])
    except Exception as e:
        print(f"Error by {str(e)}")

    # print(type(eur))
    # print()
    # return data

def main():
    start_date = datetime(2021, 9, 5)
    end_date = datetime(2021, 9, 10)
    get_info(start_date, end_date)


if __name__ == "__main__":
    main()
