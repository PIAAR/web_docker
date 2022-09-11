import sqlite3
# from multiprocessing.dummy import connection

import alpaca_trade_api as tradeapi
import _1_config 

connection = sqlite3.connect(_1_config.DB_FILE)

cursor = connection.cursor()

api = tradeapi.REST(_1_config.API_KEY, _1_config.API_SECRET_KEY, base_url=_1_config.API_URL)

# assets = api.list_assets()
assets = api.list_assets("AAPL")

print(assets)

# Asset({   
#   'class': 'us_equity',
#   'easy_to_borrow': False,
#   'exchange': 'OTC',
#   'fractionable': False,
#   'id': 'cf8941f2-c358-4c6e-b515-dba56f920bfe',
#   'marginable': False,
#   'name': 'SINOTRUK HONG KONG LTD SHS (Hong Kong)',
#   'shortable': False,
#   'status': 'inactive',
#   'symbol': 'SHKLF',
#   'tradable': False
# }) Traceback (most recent call last):

# {
#   "id": "904837e3-3b76-47ec-b432-046db621571b",
#   "class": "us_equity",
#   "exchange": "NASDAQ",
#   "symbol": "AAPL",
#   "status": "active",
#   "tradable": true,
#   "marginable": true,
#   "shortable": true,
#   "easy_to_borrow": true,
#   "fractionable": true
# }

# for asset in assets:
    
#     try:
#         if asset.status =='active' and 'asset.tradable':
#             cursor.execute("INSERT INTO stock (stock_symbol, company, exchange) VALUES (?, ?, ?)", (asset.symbol, asset.name, asset.exchange))
#             print(f"Added a new stock {asset.symbol}, {asset.name} for {asset.exchange}")
#             # Other details
#             print(f"") 
#             # cursor.execute("INSERT INTO stock_details (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
        
#     except Exception as e:
#         print(asset.symbol)
#         print(f"This asset {asset.symbol} has not been added or updated: {asset.name}...")

# Code to populate db by symbol and name on the Alpaca Market
    
connection.commit()

# print('The stock table is populated. Please run the update command to remain current.')
