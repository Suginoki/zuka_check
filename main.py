import csv
import os
import sys
import requests

import pandas as pd
from bs4 import BeautifulSoup

def scraping(url):
    req = requests.get(url)
    if req.status_code != 200 :
        return -1
    result = []
    return result

def memo(result):
    with open('memo.CSV', 'w', newline='',encoding='utf_8') as file:
        writer = csv.writer(file)
        