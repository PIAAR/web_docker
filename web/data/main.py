import sqlite3, requests
from datetime import date
import alpaca_trade_api as tradeapi
import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import _1_config

# current_date = datetime.datetime(today=datetime).isoformat()

app = FastAPI()
# Using Jinja2 Templates for UI
templates = Jinja2Templates(directory="templates")

@app.get("/")
def main(request: Request):
    # 
    head = [
        {'link_1':'<link rel="stylesheet" href="nicepage.css" media="screen">'},
        {'link_2':'<link rel="stylesheet" href="RMI-Securities.css" media="screen">'},
        {'link_3':'<script class="u-script" type="text/javascript" src="jquery.js" defer=""></script>'},
        {'link_4':'<script class="u-script" type="text/javascript" src="nicepage.js" defer=""></script>'},
        {'link_5':'<meta name="generator" content="Nicepage 4.12.21, nicepage.com">'},
        {'link_6':'<link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i">'}]
    body = []
    foot = []

    connection = sqlite3.connect(_1_config.DB_APP_FILE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, stock_symbol, company, exchange FROM stock ORDER BY stock_symbol
    """)
    rows = cursor.fetchall()

    cursor2 = connection.cursor()
    cursor2.execute("""
        SELECT * FROM stock_price ORDER BY date
    """)
    # id, stock_id, price_symbol, date, open, high, low, close, volume
    prices = cursor2.fetchall()

# RENDER THE PATH and VARIABLES
    context= {"head":head, 
        "body":body, 
        "foot":foot, 
        "request": request, 
        "prices": prices,
        "stocks": rows
        }
    return templates.TemplateResponse("/stx/index.html", context)
 
@app.get("/stocks/")
def index(request: Request):
    stock_filter = request.query_params.get('filter', False)
    # print(dir(request.headers))
    connection = sqlite3.connect(_1_config.DB_APP_FILE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    
    if stock_filter == "new_closing_highs":
        cursor.execute("""
            SELECT * from ( 
                select stock_symbol, company, stock_id, max(close), date, exchange
                from stock_price 
                join stock on stock.id = stock_price.stock_id 
                group by stock_id 
                order by close DESC) 
            where date = ?""", (date.today().isoformat(),))
        # closing_high = cursor.fetchall()
    else:
        cursor.execute("""
            SELECT id, stock_symbol, company, exchange FROM stock ORDER BY stock_symbol
        """) 
    
    rows = cursor.fetchall()

    return templates.TemplateResponse("stx/stock.html", {"request": request, "stocks": rows })

@app.get("/stocks/{stock_symbol}")
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