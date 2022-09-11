#   WEB SCRAPER #
import datetime
import sqlite3
from socket import create_connection

import requests
from bs4 import BeautifulSoup

import _1_config
# from database.data.tables import STOCK_TABLE_INFO
import tables

connection = sqlite3.connect(_1_config.DB_FILE)
cursor = connection.cursor()

# STOCKS 
class DB:
    def __init__(self, message):
        self.text = message
        # self.symbol = column1
        
    def create_stock_table(self):
        # conn_messg.create_cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS stock (
                id INTEGER PRIMARY KEY,
                stock_symbol TEXT NOT NULL UNIQUE,
                company TEXT NOT NULL,
                exchange TEXT NOT NULL
                )
        """)
    
    def create_table_stock_price(self):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS stock_price (
                id INTEGER PRIMARY KEY,
                stock_id INTEGER,
                price_symbol NOT NULL,
                date NOT NULL,
                open NOT NULL,
                high NOT NULL,
                low NOT NULL,
                close NOT NULL,
                volume NOT NULL,
                FOREIGN KEY (stock_id) REFERENCES stock (id)
        )
        """)
    
    def create_alpaca_table_stock_details(self):
        # Alpaca Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alpaca_stock_details (
                id INTEGER PRIMARY KEY,
                stock_id INTEGER,
                symbol TEXT,
                headline TEXT,
                url TEXT,
                source TEXT,
                created_date TEXT,
                summary TEXT,
                FOREIGN KEY (symbol) REFERENCES stock (stock_symbol)
            )
        """)

# def create_table_stock_details(self):
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS stock_details (
#                 id INTEGER PRIMARY KEY,
#                 stock_id INTEGER,
#                 date NOT NULL,
#                 company NOT NULL,
#                 exchange NOT NULL,
#                 trade_id NOT NULL,
#                 marginable NOT NULL,
#                 tradable NOT NULL,
#                 shortable NOT NULL,
#                 FOREIGN KEY (stock_id) REFERENCES stock (id)
#             )
#         """)

# CRYPTO
    def create_crypto_table(self):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS crypto (
                id INTEGER PRIMARY KEY,
                crypto_symbol TEXT NOT NULL UNIQUE,
                company TEXT NOT NULL,
                exchange TEXT NOT NULL
                )
        """)

    def create_table_crypto_price(self):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS crypto_price (
                id INTEGER PRIMARY KEY,
                crypto_id INTEGER,
                date NOT NULL,
                open NOT NULL,
                high NOT NULL,
                low NOT NULL,
                close NOT NULL,
                adjusted_close NOT NULL,
                volume NOT NULL,
                FOREIGN KEY (crypto_id) REFERENCES crypto (id)
            )
        """)
    
    def create_table_crypto_details(self):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS crypto_details (
                id INTEGER PRIMARY KEY,
                crypto_id INTEGER,
                date NOT NULL,
                company NOT NULL,
                exchange NOT NULL,
                trade_id NOT NULL,
                marginable NOT NULL,
                tradable NOT NULL,
                shortable NOT NULL,
                FOREIGN KEY (crypto_id) REFERENCES crypto (id)
            )
        """)
# FOREX 
    def create_forex_table(self):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS forex (
                id INTEGER PRIMARY KEY,
                forex_symbol TEXT NOT NULL UNIQUE,
                company TEXT NOT NULL,
                exchange TEXT NOT NULL
                )
        """)
    
    def create_table_forex_price(self):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS forex_price (
                id INTEGER PRIMARY KEY,
                forex_id INTEGER,
                date NOT NULL,
                open NOT NULL,
                high NOT NULL,
                low NOT NULL,
                close NOT NULL,
                adjusted_close NOT NULL,
                volume NOT NULL,
                FOREIGN KEY (forex_id) REFERENCES forex (id)
            )
        """)
    
    def create_table_forex_details(self):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS forex_details (
                id INTEGER PRIMARY KEY,
                forex_id INTEGER,
                date NOT NULL,
                company NOT NULL,
                exchange NOT NULL,
                trade_id NOT NULL,
                marginable NOT NULL,
                tradable NOT NULL,
                shortable NOT NULL,
                FOREIGN KEY (forex_id) REFERENCES forex (id)
            )
        """)
    
    def db_table_create_msg(self):
        return print(f"All tables have been created.")
    
    def connection_commit(self):
        connection.commit()

# Executions and Print Statements

# STOCKS
stock_table = DB('Stock Table Created')
stock_table.create_stock_table()
print(stock_table.text)

stock_prices = DB('Stock Prices Table Created')
stock_prices.create_table_stock_price()
print(stock_prices.text)

stock_details = DB('Alpaca Stock Details Table Created ')
stock_details.create_alpaca_table_stock_details()
print(stock_details.text)

# CRYPTO
crypto_table = DB('Crypto Table Created')
crypto_table.create_crypto_table()
print(crypto_table.text)

crypto_prices = DB('Crypto Prices Table Created')
crypto_prices.create_table_crypto_price()
print(crypto_prices.text)

crypto_details = DB('Crypto Details Table Created')
crypto_details.create_table_crypto_details()
print(crypto_details.text)

# FOREX
forex_table = DB('Forex Table Created')
forex_table.create_forex_table()
print(forex_table.text)

forex_prices = DB('Forex Prices Table Created')
forex_prices.create_table_forex_price()
print(forex_prices.text)

forex_details = DB('Forex Details Table Created')
forex_details.create_table_forex_details()
print(forex_details.text)

# tables_finished = DB('For all Tables...')
# tables_finished.db_table_create_msg()
# print(tables_finished.text)

connection.commit()
