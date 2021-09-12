"""Flask app config file"""

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pandas as pd
from .get_currency import *
from config import Config

app = Flask(__name__)


def get_environment_config():
    if Config.ENV == "TESTING":
        return "config.TestingConfig"
    
    elif Config.ENV == "DEVELOPMENT":
        return "config.DevelopmentConfig"


app.config.from_object(get_environment_config())
db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.before_first_request
def initialize_database():
    db.create_all()
    # dataframe = pd.read_csv("app/classification_data.csv")

    euro = get_info(currency="EURUSD", start_date=datetime(2021, 9, 6), end_date=datetime(2021, 9, 11))
    peso = get_info(currency="CLPUSD", start_date=datetime(2021, 9, 6), end_date=datetime(2021, 9, 11))
    soles = get_info(currency="PENUSD", start_date=datetime(2021, 9, 6), end_date=datetime(2021, 9, 11))


    euro.to_sql(name = "euro_currency", if_exists="replace", con=db.engine, index=True)
    peso.to_sql(name = "peso_currency", if_exists="replace", con=db.engine, index=True)
    soles.to_sql(name = "soles_currency", if_exists="replace", con=db.engine, index=True)


from app import routes