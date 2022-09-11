import sqlite3, requests
from datetime import date
import alpaca_trade_api as tradeapi
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

import _1_config

# current_date = datetime.datetime(today=datetime).isoformat()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    stock_filter = request.query_params.get('filter', False)
    # print(dir(request.headers))
    connection = sqlite3.connect(_1_config.DB_APP_FILE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    
    if stock_filter == "new_closing_highs":
        cursor.execute("""
            SELECT * from (
                SELECT * from ( 
                    select stock_symbol, company, stock_id, max(close), date 
                    from stock_price 
                    join stock on stock.id = stock_price.stock_id 
                    group by stock_id 
                    order by stock_symbol DESC) 
                where date = ?""", (date.today().isoformat(),))

        # closing_high = cursor.fetchall()
    else:
        cursor.execute("""
            SELECT id, stock_symbol, company, exchange FROM stock ORDER BY stock_symbol
        """) 
    
    rows = cursor.fetchall()

    return templates.TemplateResponse("index.html", {"request": request, "stocks": rows, "prices": "rows_2"})

@app.get("/stock/{stock_symbol}")
def details(request: Request, stock_symbol):    
    connection = sqlite3.connect(_1_config.DB_APP_FILE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
        
    cursor.execute("""
        SELECT id, stock_symbol, company, exchange FROM stock WHERE stock_symbol = ?
    """,(stock_symbol,))

    row = cursor.fetchone()

    cursor.execute("""
        SELECT * FROM stock_price WHERE id = ? ORDER BY date
    """, (row['id'],))

    bars = cursor.fetchall()

    return templates.TemplateResponse("details.html", {"request": request, "stock": row, "bars": bars})