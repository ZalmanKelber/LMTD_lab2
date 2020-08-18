from random import seed
from random import random

seed(1)

class Stock:
    #each stock comes with a range of possible next outcomes that corresponds more or less to associated risk,
    #although this is subject to slight changes.  Current risk can only be accessed in hindsight
    def __init__(self, name: str, risk_factor: float, initial_price: float):
        default_risk_constant = .25
        self.name = name
        self.risk_factor = min(risk_factor, 1.0) or default_risk_constant
        self.risk_elasticity = (random() * default_risk_constant) #random value between 0 and 0.25
        self.price = initial_price or 20.0

    def __str__(self):
        return "name: {0}, current price: ${price:.2f}, risk factor: {1}".format(self.name, self.risk_factor, price = self.price)

    def calculate_value(self): #stock changes price and risk factor everytime value is retrieved
        self.risk_factor = min(self.risk_factor * (1 + (random() * self.risk_elasticity * 2 - self.risk_elasticity)), 1)
        price_factor = 1 + (random() * self.risk_factor * 2 - self.risk_factor)
        self.price *= price_factor
        return self.price

    def get_value(self):
        return self.price

    def set_risk_factor(self, risk_factor: float):
        self.risk_factor = risk_factor

    def set_price(self, price: float):
        self.price = float;

class Market:
    def __init__(self):
        self.stocks = dict()

    def add_stock(self, stock_name: str, risk_factor: float, initial_price: float):
        if stock_name not in self.stocks:
            self.stocks[stock_name] = Stock(stock_name, risk_factor, initial_price)
        else:
            self.stocks[stock_name].set_risk_factor(risk_factor)
            self.stocks[stock_name].set_price(initial_price)

    def retrieve_stock(self, stock_name: str):
        return self.stocks[stock_name]

    def print_stock(self, stock_name: str):
        print(self.stocks[stock_name])

    def display_stocks(self):
        if not bool(self.stocks):
            print("no stocks to display")
        else:
            for stock in self.stocks.values():
                print(stock)

class Portfolio:
    #user interface allowing individual user to buy and sell stocks
    def __init__(self, market: Market, initial_balance: float):
        self.balance = initial_balance * 1.0
        self.market = market
        self.portfolio = dict()

    def add_cash(self, cash: float):
        self.balance += cash
        self.print_balance()

    def withdraw_cash(self, cash: float):
        if self.balance >= cash:
            self.balance -= cash
            self.print_balance()
        else:
            print("Cannot withdraw amount greater than current balance")

    def print_balance(self):
        print("Current balance: ${0:.2f}".format(self.balance))

    def print_portfolio(self):
        for stock in self.portfolio:
            quantity = float(self.portfolio[stock]["quantity"])
            value = float(self.portfolio[stock]["stock"].calculate_value())
            print("name: {0}, quantity: {1}, total value: {2:.2f}".format(stock, quantity, quantity * value))

    def buy_stock(self, stock_name: str, quantity: int):
        stock = self.market.retrieve_stock(stock_name)
        price = float(stock.get_value()) * float(quantity)
        if self.balance < price:
            print("Insufficient funds")
            return
        self.balance -= price
        if stock_name in self.portfolio:
            self.portfolio[stock_name]["quantity"] += quantity
        else:
            self.portfolio[stock_name] = {"stock": stock, "quantity": quantity}
        print("Transaction completed")
        stock.calculate_value()

    def sell_stock(self, stock_name: str, quantity: int):
        if stock_name not in self.portfolio or self.portfolio[stock_name]["quantity"] < quantity:
            print("Cannot sell more shares than you currently have")
            return
        self.buy_stock(stock_name, quantity * -1)
