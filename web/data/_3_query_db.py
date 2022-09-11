from calendar import FRIDAY, MONDAY
import sqlite3
from multiprocessing.dummy import connection

import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame

import _1_config
# # # # # # # # # # # TEST DATABASE # # # # # # # # # # # #
# DATABASE CONNECTION
connection = sqlite3.connect(_1_config.DB_FILE)
connection.row_factory = sqlite3.Row
    # CREATE SQLITE CURSOR
cursor = connection.cursor()
    # SQL STATEMENT
cursor.execute("""
    SELECT stock_symbol, company, exchange FROM stock
""")

rows = cursor.fetchall()
for row in rows:
    stock_symbol = row['stock_symbol']
    company_name = row['company']
    exchange = row['exchange']
    print(row['stock_symbol'], row['company'], row['exchange'])

# # # # # # # # # # #       TEST API       # # # # # # # # # # # #
api = tradeapi.REST(_1_config.API_KEY, _1_config.API_SECRET_KEY, base_url=_1_config.API_URL)
stocks_bars = api.list_assets()
crypto_bars = api.get_crypto_bars(stock_symbol,TimeFrame.Week, "2020-05-05", "2022-05-05")
print(stocks_bars)
print(crypto_bars)
 
# STOCKS SHOULD LOOK LIKE THIS RESPONSE
    # 'id': 'd6f1de6a-0650-4841-bc16-b0442e7da54b',
    # 'marginable': False,
    # 'min_order_size': '0.1',
    # 'min_trade_increment': '0.1',
    # 'name': 'Avalanche',
    # 'price_increment': '0.0005',
    # 'shortable': False,
    # 'status': 'active',
    # 'symbol': 'AVAXUSD',
    # 'tradable': True}), Asset({   'class': 'crypto',
    # 'easy_to_borrow': False,
    # 'exchange': 'FTXU',
    # 'fractionable': True,

# CRYPTO SHOULD LOOK LIKE THIS RESPONSE
    # 'x': 'ERSX'}), Bar({   'c': 258,
    # 'h': 302.275,
    # 'l': 254.925,
    # 'n': 7021,
    # 'o': 288.125,
    # 't': '2022-05-02T05:00:00Z',
    # 'v': 31941.313,
    # 'vw': 276.940816,
    # 'x': 'FTXU'})]

connection.commit()
