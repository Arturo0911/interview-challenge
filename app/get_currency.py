
"""Flask service to fetch the currency in 5 differents years"""

import pandas as pd
from datetime import (
    datetime,
    timedelta,
    date
)
import pandas_datareader as pdr
from pprint import pprint


# data tupes

pandas_series = pd.core.frame.DataFrame



def get_info(**kwargs) -> pandas_series:
    """The arguments would be currency, time start and end date"""
    try:

        eur = pdr.DataReader('EURUSD=X', 'yahoo', start=kwargs["start_date"], end=kwargs["end_date"])['Adj Close']
        chilean = pdr.DataReader('CLPUSD=X', 'yahoo', start=kwargs["start_date"], end=kwargs["end_date"])['Adj Close']
        peruvian = pdr.DataReader('PENUSD=X', 'yahoo', start=kwargs["start_date"], end=kwargs["end_date"])['Adj Close']


        eur_ = [x for x in eur.to_numpy()]
        chilean_ = [x for x in chilean.to_numpy()]
        peruvian_ = [x for x in peruvian.to_numpy()]


        parsed = pd.DataFrame(eur)
        dates = [pd.to_datetime(str(x)).strftime('%Y.%m.%d') for x in eur.index.to_numpy()]

        return pd.DataFrame({"datetime": dates, "euro_currency": eur_, "chilean_currency": chilean_, "peruvian_currency":peruvian_ })
    except Exception:
        return None



# def main():
#     print(get_info(start_date=datetime(2021, 9, 6), end_date=datetime(2021, 9, 11)))
