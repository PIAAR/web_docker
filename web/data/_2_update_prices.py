import sqlite3
from multiprocessing.dummy import connection

import alpaca_trade_api as tradeapi

import _1_config

connection = sqlite3.connect(_1_config.DB_FILE)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("""
    SELECT id, stock_symbol, company FROM stock
""")

rows = cursor.fetchall()
symbols = [row['stock_symbol'] for row in rows]
stock_dict = {}         # symbols = []
for row in rows:
    symbol = row['stock_symbol']
    symbols.append(symbol) 
    stock_dict[symbol] = row['id']
    
#     print(row['stock_symbol'], row['company'])
# symbols = [row['stock_symbol'] for row in rows]

api = tradeapi.REST(_1_config.P_API_KEY, _1_config.P_API_SECRET_KEY, base_url=_1_config.API_URL)

chunk_size = 200

for i in range(0, len(symbols), chunk_size):
    symbol_chunk = symbols[i:i+chunk_size]
    barsets = api.get_bars(symbol_chunk,'1Day')
    
    for symbol in barsets:
        print(f"processing symbol {symbol}")
        for bar in barsets[symbol]:
            print(bar.t, bar.o, bar.h, bar.l, bar.c, bar.v)
            stock_id = stock_dict[symbol]
            # cursor.execute("""
            #         INSERT INTO stock_price (stock_id, date, open, high, low, close, adjusted_close, volume) 
            #         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            # """, (stock_id, bar.t.date(), bar.o, bar.h, bar.l, bar.c, bar.c, bar.v))

print(f"The prices are updated.")   
connection.commit()
