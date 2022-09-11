import sqlite3
import _1_config
import tables


connection = sqlite3.connect(_1_config.DB_FILE)

cursor = connection.cursor()

cursor.execute("DELETE FROM stock")

# price = tables.STOCK_TABLE_NUMBERS
# cursor.execute("DELETE FROM (?)", (price))
cursor.execute("DELETE FROM stock_price")

cursor.execute("DELETE FROM stock_details")

cursor.execute("DELETE FROM crypto")

cursor.execute("DELETE FROM crypto_price")

cursor.execute("DELETE FROM crypto_details")

cursor.execute("DELETE FROM forex")

cursor.execute("DELETE FROM forex_price")

cursor.execute("DELETE FROM forex_details")

connection.commit()

print(f"The table data has been deleted.")