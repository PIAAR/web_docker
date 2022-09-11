import chunk
import sqlite3, datetime
from multiprocessing.dummy import connection
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit

import _1_config
# from 0_db import DB  # Run your other file
class Details:
        connection = sqlite3.connect(_1_config.DB_FILE)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        # api = tradeapi.REST(_1_config.API_KEY, _1_config.API_SECRET_KEY, base_url=_1_config.API_URL)
        news_api = tradeapi.REST(_1_config.L_API_KEY, _1_config.L_API_SECRET_KEY, base_url=_1_config.NEWS_URL)
        chunk_size = 200

        start_date = "2021-05-01"   # Initiate Date
        current_date = datetime.datetime.now()
        # end_date = "2022-05-05"
        end_date = current_date
        # print(barsets)
        # Time_Frame_config = [TimeFrame(1, TimeFrameUnit.Month), start_date, current_date]
        Time_Frame_config = [TimeFrame(1, TimeFrameUnit.Hour), start_date, current_date]
        # Time_Frame_config = [TimeFrame(59, TimeFrameUnit.Minute), start_date, current_date]
        # Time_Frame_config = [TimeFrame.Hour, start_date, current_date]
        # Time_Frame_config = [TimeFrame.Day, "2020-06-08", "2021-06-08"]
        print(f"The start date is {start_date} and the end date is {end_date}")

        def __init__(self,msg):
            return print(msg)
            
        def get_stock_list():
            Details.cursor.execute("""
                    SELECT id, stock_symbol, company FROM stock
                """)
            rows = Details.cursor.fetchall()

            symbols = [row['stock_symbol'] for row in rows]
            stock_dict = {}

            for row in rows:
                symbol = row['stock_symbol']
                symbols.append(symbol)
                stock_dict[symbol] = row['id']
                # print(symbol, row['company'])

        def processed_details():    
            for i in range(0, len(Details.symbols), Details.chunk_size):
                symbol_chunk = Details.symbols[i:i+Details.chunk_size]
                db_message = Details.symbols.count
                # API call to get data for each symbol
                news_sets = Details.news_api.get_news(symbol_chunk)
                # print(news_sets)
                for news in news_sets:
                    print(f"processing symbol... {symbol}")
                    stock_id = str(news.id)
                    symbol = str(news.symbols)
                    source = str(news.source)
                    summary = str(news.summary)
                    headline = str(news.headline)
                    created_date = str(news.created_at)
                    url = str(news.url)
                    print(f"processing news for... {'AAPL'}")
                    print(stock_id,symbol,headline,url,source,created_date,summary)

                    # INSERT into TABLE
                    Details.cursor.execute("""
                        INSERT INTO alpaca_stock_details (stock_id,symbol,headline,url,source,created_date,summary) 
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """, (stock_id,symbol,headline,url,source,created_date,summary))
                    
                    print("The news has been processed!!!")
                    connection.commit()


date = datetime.datetime.now()
date_str = date.strftime("%A")
for i in range(0, 10000, 1):
    file = i
    path = "./database/data/db/_db_stock_details.txt"
f = open(str(path), "a")
f.write(str("Updated the News at ..."))
f.close()

g = open(str(path), "a")
g.write(str(date))
g.write("\n")
g.close()

print(f"The news is updated")