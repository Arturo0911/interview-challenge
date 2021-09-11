#!/usr/bin/python

from typing import Any
from bs4 import BeautifulSoup
from pprint import pprint
import requests

URL_HOST = "https://finance.yahoo.com/currency-converter"
FATHER_SHAPE = "responsive-layout-portrait"


def parsing_html(url_text: Any):
    parsed = BeautifulSoup(url_text, 'html.parser')

    pprint(parsed.find("table").find("tbody").find_all("tr"))
    # pprint(parsed.find_all(attrs={"class": "responsive-layout-portrait"}))


def main():
    res = requests.get(url=URL_HOST)
    parsing_html(res.text)


if __name__ == "__main__":
    main()
