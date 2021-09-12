
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

        eur = pdr.DataReader(kwargs["currency"]+'=X', 'yahoo', start=kwargs["start_date"], end=kwargs["end_date"])['Adj Close']
        parsed = pd.DataFrame(eur)
        dates = [pd.to_datetime(str(x)).strftime('%Y.%m.%d') for x in eur.index.to_numpy()]
        currencys = [x[0] for x in parsed.to_numpy()]

        return pd.DataFrame({"datetime": dates, "currencys": currencys})
    except Exception:
        return None
