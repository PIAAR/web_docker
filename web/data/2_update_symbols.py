import sqlite3

import alpaca_trade_api as tradeapi

import _1_config

# from database.data.config import API_KEY, API_SECRET_KEY, API_URL

class Update:
    connection = sqlite3.connect(_1_config.DB_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    api = tradeapi.REST(_1_config.P_API_KEY, _1_config.P_API_SECRET_KEY, base_url=_1_config.API_URL)
    
    def __init__(self, message):
        self.text = message
        self.connection = Update.connection
        self.api = Update.api
        self.cursor = Update.cursor
        self.row_factory = Update.connection.row_factory

    def get_symbols(self):
        self.cursor.execute("""
            SELECT stock_symbol, company FROM stock
            """)
        rows = self.cursor.fetchall()
        self.symbols = [row['stock_symbol'] for row in rows]
        self.assets = self.api.list_assets()

        print(f"Checking for updates...")
        for asset in self.assets:
            
            try: 
                if (asset.symbol not in self.symbols) and (asset.status =='active' and 'asset.tradable'):
                    val_update = 0
                    Update.cursor.execute("INSERT INTO stock (stock_symbol, company, exchange) VALUES (?, ?, ?)", (asset.symbol, asset.name, asset.exchange))
                    print(f"Added a new stock {asset.symbol}, {asset.name} for {asset.exchange}")
            
                        # print(f"Added a new stock {asset.symbol} {asset.name}")
                    
            except Exception as e:
                val_update = 1
                print(asset.symbol)
                print(f"This asset {asset.symbol} has not been added or updated: {asset.name} has a update value of {val_update}...")
                print(e)

        print(f"There are no updates to the stock list.")


        # Code to populate db by symbol and name on the Alpaca Market
            
        self.connection.commit()

update_message = Update("The symbols are updated")
update_message.get_symbols()
print(update_message.text)


#################################################################
# symbols = []
# for row in rows:
#     # symbols.append(row['symbol'], row['company'])
#     print(row['symbol'], row['company'])


# Asset({   'class': 'us_equity',
#     'easy_to_borrow': False,
#     'exchange': 'OTC',
#     'fractionable': False,
#     'id': 'cf8941f2-c358-4c6e-b515-dba56f920bfe',
#     'marginable': False,
#     'name': 'SINOTRUK HONG KONG LTD SHS (Hong Kong)',
#     'shortable': False,
#     'status': 'inactive',
#     'symbol': 'SHKLF',
#     'tradable': False})Traceback (most recent call last):