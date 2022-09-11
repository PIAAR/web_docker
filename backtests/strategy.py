# RMG strategy is to:
# - run a bot that will trade STOCKS, CRYPTO, and FOREX
# STOCKS - 
#   from Bianance
#   from Alpaca
#   from Yfinance
# 

from asyncore import read
from tracemalloc import start
from typing_extensions import Self


class Strategy:    
    market_class = [
        {'market':['stock','crypto','forex']}
        ]
    green = 'green_light'
    
    def __init__(self):
        go_flag = Strategy.green

    def stocks(self):
        if Strategy.go_flag == True:
            self.light  == Strategy.green
            return self.light

    def crypto(self):
        pass
    
    def forex(self):
        pass






