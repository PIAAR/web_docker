# Imports missing
import requests
# from .config import *
# from configu import *
import configu

import alpaca_trade_api as api

ACCOUNT_URL = "{}/v2/account".format(configu.BASE_URL)

r = requests.get(ACCOUNT_URL, headers={'KEY_ID':configu.API_KEY,'SECRET':configu.API_SECRET}) 
print(r.content)

# alpaca_client = api.REST(configu.API_KEY, configu.API_SECRET, configu.BASE_URL)

# symbol = "BTCUSD" 
# timeframe = "1Day"
# start = "2022-01-01"
# end = "2022-01-31"

# btc_bars = alpaca_client.get_crypto_bars(symbol, timeframe, start, end).df
# print(btc_bars.head())