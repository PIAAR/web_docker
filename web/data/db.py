#   WEB SCRAPER #
import sqlite3

import requests
from bs4 import BeautifulSoup

import _1_config
# from database.data.tables import STOCK_TABLE_INFO
import tables

connection = sqlite3.connect(_1_config.DB_FILE)

cursor = connection.cursor()

# STOCKS 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY,
        symbol TEXT NOT NULL UNIQUE,
        company TEXT NOT NULL
        )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_price (
        id INTEGER PRIMARY KEY,
        stock_id INTEGER,
        date NOT NULL,
        open NOT NULL,
        high NOT NULL,
        low NOT NULL,
        close NOT NULL,
        volume NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_details (
        id INTEGER PRIMARY KEY,
        stock_id INTEGER,
        date NOT NULL,
        company NOT NULL,
        exchange NOT NULL,
        trade_id NOT NULL,
        marginable NOT NULL,
        tradable NOT NULL,
        shortable NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
    )
""")

# CRYPTO

cursor.execute("""
    CREATE TABLE IF NOT EXISTS crypto (
        id INTEGER PRIMARY KEY,
        symbol TEXT NOT NULL UNIQUE,
        company TEXT NOT NULL
        )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS crypto_price (
        id INTEGER PRIMARY KEY,
        stock_id INTEGER,
        date NOT NULL,
        open NOT NULL,
        high NOT NULL,
        low NOT NULL,
        close NOT NULL,
        adjusted_close NOT NULL,
        volume NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS crypto_details (
        id INTEGER PRIMARY KEY,
        stock_id INTEGER,
        date NOT NULL,
        company NOT NULL,
        exchange NOT NULL,
        trade_id NOT NULL,
        marginable NOT NULL,
        tradable NOT NULL,
        shortable NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
    )
""")

# FOREX 

cursor.execute("""
    CREATE TABLE IF NOT EXISTS forex (
        id INTEGER PRIMARY KEY,
        symbol TEXT NOT NULL UNIQUE,
        company TEXT NOT NULL
        )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS forex_price (
        id INTEGER PRIMARY KEY,
        stock_id INTEGER,
        date NOT NULL,
        open NOT NULL,
        high NOT NULL,
        low NOT NULL,
        close NOT NULL,
        adjusted_close NOT NULL,
        volume NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS forex_details (
        id INTEGER PRIMARY KEY,
        stock_id INTEGER,
        date NOT NULL,
        company NOT NULL,
        exchange NOT NULL,
        trade_id NOT NULL,
        marginable NOT NULL,
        tradable NOT NULL,
        shortable NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
    )
""")

connection.commit()

print(f"All tables have been created.")
