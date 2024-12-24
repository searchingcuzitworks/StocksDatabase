# Modules
import pandas as pd
import json
import requests
from urllib.request import urlopen
import certifi

# Algrorithm - All stocks in NSE
def nse_stocks():
    url = "https://financialmodelingprep.com/api/v3/symbol/NSE?apikey=kOA329x0FUKk3nBlZAh3w9vFECMRkdi5"
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    data = json.loads(data)
    df = pd.DataFrame(data)
    df = df.drop(columns = ["earningsAnnouncement", "timestamp"])
    return df