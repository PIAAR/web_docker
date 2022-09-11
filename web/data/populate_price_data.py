import chunk
import sqlite3, datetime
from multiprocessing.dummy import connection
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit

import _1_config

connection = sqlite3.connect(_1_config.DB_FILE)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()
cursor.execute("""SELECT id, stock_symbol, company, exchange FROM stock""")
rows = cursor.fetchall()
symbols = [row['stock_symbol'] for row in rows]
stock_dict = {}

for row in rows:
    symbol = row['stock_symbol']
    symbols.append(symbol)
    stock_dict[symbol] = row['id']
    # print(symbol, row['company'])

def process_bar(bar):
    # process bar
    print(bar)

api = tradeapi.REST(_1_config.P_API_KEY, _1_config.P_API_SECRET_KEY, base_url=_1_config.API_URL)
# news_api = tradeapi.REST(_1_config.API_KEY, _1_config.API_SECRET_KEY, base_url=_1_config.NEWS_URL)
chunk_size = 1

start_date = "2021-05-01"   # Initiate Date
current_date = datetime.datetime.now()
end_date = "2021-06-05"
# end_date = current_date
# print(current_date) 
Time_Frame_config = [TimeFrame(1, TimeFrameUnit.Day), start_date, end_date]
# Time_Frame_config = [TimeFrame(1, TimeFrameUnit.Hour), start_date, current_date]
# Time_Frame_config = [TimeFrame.Day, "2020-06-08", "2021-06-08"]
# barsets = api.get_bars(symbols, Time_Frame_config)
count_symbols = len(symbols)
print (f"The start date is {start_date} and the end date is {end_date}")

for i in range(0, count_symbols, chunk_size):
    symbol_chunk = symbols[i:i+chunk_size]
    # API call to get data for each symbol
    barsets = api.get_bars(symbol_chunk, Time_Frame_config)
    # print(barsets)
    
    if barsets == []:
        for bar in barsets:
            symbol = symbols[i]
        print (f"There is no data for {symbol}")

    else:    
        for bars in barsets:
            # process_bar(bars)       # Print to Console
            symbol = bars.S
            # print(f"processing bar {bars.S}")
            # print(bars.S, bars.t, bars.o, bars.h, bars.l, bars.c, bars.v)
            stock_id = stock_dict[symbol]
            # INSERT into TABLE
            cursor.execute("""
                INSERT INTO stock_price (stock_id, price_symbol, date, open, high, low, close, volume) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (stock_id, symbol, bars.t.date(), bars.o, bars.h, bars.l, bars.c, bars.v))
            print(f"processing symbol... {symbol}")

print(f"The {count_symbols} prices are entered into the database.")   
connection.commit()
