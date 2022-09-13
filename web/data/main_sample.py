import sqlite3
import requests
import uvicorn

# import alpaca_trade_api as tradeapi
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

import _1_config

# To start web application in terminal... run the uvicorn server 
# :uvicorn main:app --reload

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    print(request)
    # return {"title": "Dashboard"}
    # from database.data.config import API_KEY, API_SECRET_KEY, API_URL
    connection = sqlite3.connect(_1_config.DB_FILE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, stock_symbol, company FROM stock
    """)
    rows = cursor.fetchall()
    
    return templates.TemplateResponse("index.html", {"request": request, "stocks": rows})
    # return {"title": "Dashboard", "stocks": rows}