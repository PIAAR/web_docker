# init

class Update:

    def __init__(self) -> None:
        stock = True
        crypto = False
        forex = False
    
        self.stock = stock
        self.crypto = crypto
        self.forex = forex
        return None

    def make_db(self, db):
        self.db = db
        return None

    def populate_db(self, db):
        pass

    def price_db(self,db):
        pass
    
    def news_db(self,db):
        pass

    def destroy_db(self,db):
        pass

class Filter:
    def __init__(self):
        pass

    def analyze_db(self,db):
        self.indicator
        pass

class Trade:
    def __init__(self):
        pass

    def trade(self, table):
        pass

class No_Trade:
    def __init__(self):
        pass

    def stop_trading(self, table):
        pass

class Mange:
    def __init__(self):
        pass

    def count_money(self, account):
        pass

    def move_money_in(self, account):
        pass

    def move_money_out(self, account):
        pass

    def split_money(self, account_1, account_2):
        pass
