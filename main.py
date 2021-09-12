#!/usr/bin/python

"""
@author Arturo Negreiros Samanez
This code base was creted to automatice fetch the current change
and store in database
"""

import pandas as pd
from datetime import (
    datetime,
    timedelta,
    date
)
import pandas_datareader as pdr
from pprint import pprint


def get_info(**kwargs) -> pd.DataFrame:
    """The arguments would be currency, time start and end date"""
    try:

        eur = pdr.DataReader(kwargs["currency"]+'=X', 'yahoo', start=kwargs["start_date"], end=kwargs["end_date"])['Adj Close']
        parsed = pd.DataFrame(eur)
        dates = [pd.to_datetime(str(x)).strftime('%Y.%m.%d') for x in eur.index.to_numpy()]
        currencys = [x[0] for x in parsed.to_numpy()]

        return pd.DataFrame({"datetime": dates, "currencys": currencys})
    except Exception:
        return


def main():

    print(get_info(currency="CLPUSD", start_date=datetime(2021, 9, 6), end_date=datetime(2021, 9, 11)))


if __name__ == "__main__":
    main()
