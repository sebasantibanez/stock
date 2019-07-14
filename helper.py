import requests
website_url = requests.get('https://www.netfonds.no/quotes/exchange.php?exchange=O').text
from bs4 import BeautifulSoup

soup = BeautifulSoup(website_url,'lxml')

import pandas as pd

url = 'https://www.quandl.com/api/v3/databases/EOD/metadata?#api_key=5czsVZzyn5zaXksb31tF'
tickers = pd.read_csv(url, engine='python', compression='zip')


def ticker():
    url = 'https://www.quandl.com/api/v3/databases/EOD/metadata?#api_key=5czsVZzyn5zaXksb31tF'
    tickers = pd.read_csv(url, engine='python', compression='zip')
    return tickers

import pandas as pd
import requests

s=requests.get(url).content
c=pd.read_csv(s)