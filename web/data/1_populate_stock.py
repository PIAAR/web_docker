import sqlite3
from multiprocessing.dummy import connection
import alpaca_trade_api as tradeapi
import _1_config

class Populate:
    connection = sqlite3.connect(_1_config.DB_FILE)
    # Create cursor
    cursor = connection.cursor()
    api = tradeapi.REST(_1_config.P_API_KEY, _1_config.P_API_SECRET_KEY, base_url=_1_config.API_URL)

    def __init__(self, done_msg):
        self.assets = Populate.api.list_assets()
        self.text = done_msg
        self.cursor = Populate.cursor

    def get_stock(self):
        for asset in self.assets:
            
            try:
                if asset.status =='active' and 'asset.tradable':
                    val_update = 0
                    self.cursor.execute("INSERT INTO stock (stock_symbol, company, exchange) VALUES (?, ?, ?)", (asset.symbol, asset.name, asset.exchange))
                    print(f"Added a new stock {asset.symbol}, {asset.name} for {asset.exchange}")
                    # Other details
                    print(f"") 
                    # cursor.execute("INSERT INTO stock_details (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
                
            except Exception as e:
                val_update = 1
                print(asset.symbol)
                print(f"This asset {asset.symbol} has not been added or updated: {asset.name} has a update value of {val_update}...")

        # Code to populate db by symbol and name on the Alpaca Market
            
        self.connection.commit()

        print(f'The stock table is populated. Please run the update command to remain current.')

update_message = Populate("The table symbols are populated")
update_message.get_stock()
print(update_message.text)