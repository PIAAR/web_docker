import sqlite3

import requests
from bs4 import BeautifulSoup

import _1_config
import tables

connection = sqlite3.connect(_1_config.DB_FILE)

cursor = connection.cursor()

# User Name
# Password, 
# Api keys, Bank rtn, Bank act, 

# Url, port, login, ETL

# Indicators, Math_functions(generators, multiplexing), Datasets

# html, load_data, kill_data

class App:
    
    def __init__(self, database, user_name, user_password) -> None:
        self.name = database
        self.connection = connection.set_trace_callback
        self.user = user_name
        self.password = user_password
        
    def make_db(self):
        return '{} {}'.format(self.name, self.connection)

class Database:
    def __init__(self, database_name) -> None:
        self.database_name = database_name
        
    def show_db(self):
        pass
    
    def populate_db(self):
        import _1_db
        

class Tables:
    
    def __init__(self, table_name) -> None:
        self.table_name = table_name
        # cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS TABLE_NAME (
        #         id INTEGER PRIMARY KEY,
        #         symbol TEXT NOT NULL UNIQUE,
        #         company TEXT NOT NULL
        #         )
        # """)
        
App_Database = App('Finance', 'Gnuborn', 'Pass')
Database_1 = Database('Data')        
table_stock = Tables('stock')
table_crypto = Tables('crypto')
table_forex = Tables('forex')
print(App_Database.connection)
print(Database_1.database_name)
print(table_stock.table_name)
print(table_crypto.table_name)
print(table_forex.table_name)


