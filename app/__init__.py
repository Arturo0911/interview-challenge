"""Flask app config file"""

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pandas as pd
from .get_currency import *
# from config import Config

app = Flask(__name__)


# def get_environment_config():
#     if Config.ENV == "TESTING":
#         return "config.TestingConfig"
    
#     elif Config.ENV == "DEVELOPMENT":
#         return "config.DevelopmentConfig"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://payload_root:@localhost/PythonChallenge'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config.from_object(get_environment_config())
db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.before_first_request
def initialize_database():
    db.create_all()
    # dataframe = pd.read_csv("app/classification_data.csv")

    dataset = get_info(start_date=datetime(2021, 9, 6), end_date=datetime(2021, 9, 11))
    dataset.to_sql(name = "python_challenge", if_exists="replace", con=db.engine, index=True)

    

from app import routes
from app import models
from app import Schema