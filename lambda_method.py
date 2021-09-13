#!/usr/bin/python

from datetime import datetime
import requests
import time
from pprint import pprint
import dweepy
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    Float,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://payload_root:@localhost/PythonChallenge2')
Base = declarative_base()


class PythonChallenge2(Base):
    __tablename__ = "weather_data"

    index = Column(Integer(), primary_key=True)
    created_at = Column(DateTime(), default=datetime.now())
    temperature = Column(Float(), nullable=False, unique=True)
    humidity = Column(Float(), nullable=False, unique=True)


    def __str__(self):
        return self.index
session_maker = sessionmaker(engine)
session = session_maker()


THING_NAME = "thecore"
URL_REQUEST = "https://dweet.io/follow/thecore"


def get_weather_data():

    # time.sleep(60)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    fetched = dweepy.get_dweets_for(THING_NAME)

    lambda_x = lambda fetch: {
        "temperature": round(sum([x["content"]["temperature"] for x in fetch])/len([x["content"]["temperature"] for x in fetch]), 2),
        "humidity":round(sum([x["content"]["humidity"] for x in fetch])/len([x["content"]["humidity"] for x in fetch]), 2)
        }; time.sleep(1)
    print(lambda_x(fetched))
    # humidity = [x["content"]["humidity"] for x in ((dweepy.get_dweets_for(THING_NAME)))]

    # "humidity":[x["content"]["humidity"]]

    #print(weather)
    #print(humidity)

    # for x in dweepy.get_dweets_for(THING_NAME):
    #     print(x["content"]["temperature"])

get_weather_data()