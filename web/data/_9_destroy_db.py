from email import message
import sqlite3, os
import _1_config

connection = sqlite3.connect(_1_config.DB_FILE)

cursor = connection.cursor()
class Destroy:
    def __init__(self, message):
        self.text = message
    
    def drop_stock_table(self):
        cursor.execute("""
            DROP TABLE IF EXISTS stock
        """)

    def drop_stock_price_table(self):
        cursor.execute("""
            DROP TABLE IF EXISTS stock_price
        """)

    def drop_stock_details_table(self):
        cursor.execute("""
            DROP TABLE IF EXISTS stock_details
        """)
    
    def drop_alpaca_stock_details_table(self):
        cursor.execute("""
            DROP TABLE IF EXISTS alpaca_stock_details
        """)

    def drop_crypto_table(self):
        cursor.execute("""
            DROP TABLE IF EXISTS crypto
        """)
    
    def drop_crypto_prices_table(self):
        cursor.execute("""
            DROP TABLE IF EXISTS crypto_price
        """)
    
    def drop_crypto_details_table(self):
        cursor.execute("""
            DROP TABLE IF EXISTS crypto_details
        """)
    
    def drop_forex_table(self):
        cursor.execute("""
            DROP TABLE IF EXISTS forex
        """)

    def drop_forex_prices(self):
        cursor.execute("""
            DROP TABLE IF EXISTS forex_price
        """)

    def drop_forex_details(self):
        cursor.execute("""
            DROP TABLE IF EXISTS forex_details
        """)

    def connection_commit(self):
        connection.commit()

    def db_table_create_msg(self):
        print(f"All tables have been dropped.")
        
drop_stock_table = Destroy('The stock table has been dropped.')
drop_stock_table.drop_stock_table()
print(drop_stock_table.text)

drop_stock_price = Destroy('The stock prices table has been dropped.')
drop_stock_price.drop_stock_price_table()
print(drop_stock_price.text)

drop_stock_details = Destroy('The stock details table has been dropped.')
drop_stock_details.drop_stock_details_table()
print(drop_stock_details.text)

drop_alpaca_stock_details = Destroy('The Alpaca stock details table has been dropped.')
drop_alpaca_stock_details.drop_alpaca_stock_details_table()
print(drop_alpaca_stock_details.text)

drop_crypto_table = Destroy('The crypto table has been dropped.')
drop_crypto_table.drop_crypto_table()
print(drop_crypto_table.text)

drop_crypto_prices = Destroy('The crypto prices table has been dropped.')
drop_crypto_prices.drop_crypto_prices_table()
print(drop_crypto_prices.text)

drop_crypto_details = Destroy('The crypto details table has been dropped.')
drop_crypto_details.drop_crypto_details_table()
print(drop_crypto_details.text)

drop_forex_table = Destroy('The forex table has been dropped.')
drop_forex_table.drop_forex_table()
print(drop_forex_table.text)

drop_forex_prices = Destroy('The forex prices table has been dropped.')
drop_forex_prices.drop_forex_prices()
print(drop_forex_prices.text)

drop_forex_details = Destroy('The forex details table has been dropped.')
drop_forex_details.drop_forex_details()
print(drop_forex_details.text)

os.remove(_1_config.DB_FILE)