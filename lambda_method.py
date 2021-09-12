#!/usr/bin/python


import unittest
import requests
import time
from pprint import pprint
import dweepy
# from bs4 import BeautifulSoup as beauty
# from selenium import webdriver

THING_NAME = "thecore"
URL_REQUEST = "https://dweet.io/follow/thecore"


def get_weather_data():

    time.sleep(60)
    print([ [x["content"]["temperature"],x["content"]["humidity"]] for x in ((dweepy.get_dweets_for(THING_NAME)))])

    # for x in dweepy.get_dweets_for(THING_NAME):
    #     print(x["content"]["temperature"])

get_weather_data()