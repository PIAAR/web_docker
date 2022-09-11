import chunk
import datetime
import sqlite3
from multiprocessing.dummy import connection
from webbrowser import get
# from time import sleep

import alpaca_trade_api as tradeapi
# from alive-progress import alive_bar
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit

# from progress import bar
# from progress.bar import Bar
import _1_config


class Prices:
    connection = sqlite3.connect(_1_config.DB_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    api = tradeapi.REST(_1_config.P_API_KEY, _1_config.P_API_SECRET_KEY, base_url=_1_config.API_URL, api_version='v2')
    # api = tradeapi.REST(api_version='v2')
    # news_api = tradeapi.REST(_1_config.API_KEY, _1_config.API_SECRET_KEY, base_url=_1_config.NEWS_URL)
    chunk_size = 500

    start_date = "2021-05-01"   # Initiate Date
    current_date = datetime.datetime.now()
    end_date = "2022-01-07"
    # end_date = current_date
    # print(current_date) 
    Time_Frame_config = [TimeFrame(1, TimeFrameUnit.Hour), start_date, current_date]
    # Time_Frame_config = [TimeFrame(1, TimeFrameUnit.Hour), start_date, current_date]
    # Time_Frame_config = [TimeFrame.Day, "2020-06-08", "2021-06-08"]
    # barsets = api.get_bars(symbols, Time_Frame_config)
    # print(f"The {Prices.get_stock_list.count_symbols} prices are entered into the database.")   
    print(f"The start date is {start_date} and the end date is {end_date}")
    # current_date = Time_Frame_config
    
    def __init__(self,msg):
        return print(msg)
    
    @classmethod
    def process_bar(cls):           # process bar
        with alive_bar(26, dual_line=True, title='Populate') as bar:
        # with alive_bar(100) as bar:   # default setting
            for i in range(100):
                sleep(0.03) 
                bar()  

    def get_stock_list():
            # Symbol placeholders
        symbol_0 = "There is no symbols"
        symbol_1 = "Placeholder"
        date_processing = ""
        Prices.cursor.execute("""SELECT id, stock_symbol, company, exchange FROM stock""")
        rows = Prices.cursor.fetchall()
        symbols = [row['stock_symbol'] for row in rows]
        stock_dict = {}
        count_symbols = len(symbols)
        print(f"There are {count_symbols} symbols to process... Please wait.")

        for row in rows:
            symbol = row['stock_symbol']
            symbols.append(symbol)
            stock_dict[symbol] = row['id']
            # print(symbol, row['company'])

        try:
            for i in range(0, count_symbols, Prices.chunk_size):
                symbol_chunk = symbols[i:i+Prices.chunk_size]
                # API call to get data for each symbol
                barsets = Prices.api.get_bars(symbol_chunk, Prices.Time_Frame_config)
                
                if barsets == []:
                    for bars in barsets:
                        symbol_0 = bars.S
                        print (f'There is no data here')

                    if symbol_0 == '':
                        print (f"There is no data for {symbol_0}.")

                    else:
                        pass

                else:
                    # print(barsets)
                    # Prices.process_bar()
                    for bars in barsets:
                        symbol_1 = bars.S
                        date_processing = str(bars.t.date)
                        # print(f"processing bar {bars.S}")
                        # print(bars.S, bars.t, bars.o, bars.h, bars.l, bars.c, bars.v)
                        stock_id = stock_dict[symbol_1] 
                        # INSERT into TABLE
                        print(f"processing symbol... {symbol_1} for {date_processing}")
                        Prices.cursor.execute("""
                            INSERT INTO stock_price (stock_id, price_symbol, date, open, high, low, close, volume) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                            """, (stock_id, symbol_1, bars.t.date(), bars.o, bars.h, bars.l, bars.c, bars.v))
                        # Prices.process_bar()       # Print to Console
                    print(f"The {count_symbols} prices are processed!")

        except Exception as e:
            print(symbol_0, symbol_1, symbol, bars.S)
            print(f"This asset {symbol} has not been added or updated...")
            print(e)

        Prices.connection.commit()
    
# EXECUTION
Prices.get_stock_list()

