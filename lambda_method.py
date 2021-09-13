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
import json



engine = create_engine('mysql+mysqlconnector://payload_root:@localhost/PythonChallenge2')
Base = declarative_base()


class PythonChallenge2(Base):
    __tablename__ = "weather_data"

    index = Column(Integer(), primary_key=True)
    created_at = Column(DateTime(), default=datetime.now())
    temperature = Column(Float(), nullable=False)
    humidity = Column(Float(), nullable=False)


    def __str__(self):
        return self.index
session_maker = sessionmaker(engine)
session = session_maker()


THING_NAME = "thecore"
URL_POST = "https://webhook.site/4ed54cff-41ba-423e-9f46-b2c87408daf9"

def get_weather_data():

    # time.sleep(60)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    for x in range(15):
        fetched = lambda x: dweepy.get_dweets_for(x)

        lambda_x = lambda fetch: {
            "temperature": round(sum([x["content"]["temperature"] for x in fetch])/len([x["content"]["temperature"] for x in fetch]), 2),
            "humidity":round(sum([x["content"]["humidity"] for x in fetch])/len([x["content"]["humidity"] for x in fetch]), 2)
            }
        elements = lambda_x(fetched(THING_NAME))
        challenge_2 = PythonChallenge2(temperature=elements["temperature"], humidity=elements["humidity"])
        session.add(challenge_2)
        session.commit()
        time.sleep(60)

    weather_elements = session.query(PythonChallenge2.temperature, PythonChallenge2.humidity).all()

    body = {"data": [{"temperature": x[0], "humidity": x[1]} for x in weather_elements]}
    lambda_req = lambda data: requests.post(url=URL_POST, data=json.dumps(data), 'Content-type: Application/json')
    lambda_req(body).text

get_weather_data()