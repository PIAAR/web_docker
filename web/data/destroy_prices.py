import sqlite3
import _1_config
import tables


connection = sqlite3.connect(_1_config.DB_FILE)

cursor = connection.cursor()

cursor.execute("DELETE FROM stock_price")

cursor.execute("DROP TABLE stock_price")

connection.commit()

print(f"The table data has been deleted.")