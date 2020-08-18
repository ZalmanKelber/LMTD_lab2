import sys
from portfolio import Market, Portfolio

class Menu:
    #user interface to interact that guides interaction with portfolio
    def __init__(self, market: Market, initial_balance: float):
        self.portfolio = Portfolio(market, initial_balance)
        self.choices = [
        {"name": "exit", "action": self.exit},
        {"name": "check current balance", "action": self.portfolio.print_balance},
        {"name": "add or withdraw cash", "action": self.cash_interface},
        {"name": "view all available stocks on the market", "action": self.portfolio.market.display_stocks},
        {"name": "view your current portfolio", "action": self.portfolio.print_portfolio},
        {"name": "buy and sell stocks", "action": self.stock_interface}
        ]

    def display_greeting(self):
        print("\n\n*********************")
        print("Welcome to Python Portfolio, your personal interface with our stimulated Stock Market!")

    def display_menu(self):
        print("\nHow would you like to proceed?\n\n")
        for i in range(len(self.choices)):
            print("to {0}, enter {1}\n".format(self.choices[i]["name"], i))

    def run(self):
        self.display_greeting()
        while True:
            self.display_menu()
            choice = input("Enter selection: ")
            print("\n")
            try:
                action = self.choices[int(choice)]["action"]
            except:
                print("Invalid selection.  Please enter a number between 0 and {0}".format(len(self.choices)))
                break
            action()

    def cash_interface(self):
        choice = input("Do you wish to deposit or withdraw cash?  (enter 0 for main menu) ")
        if choice == 0 or ("deposit" not in choice.lower() and "withdraw" not in choice.lower()):
            return
        deposit = True if "deposit" in choice.lower() else False
        cash = input("How much cash do you wish to {0}? ".format("deposit" if deposit else "withdraw"))
        if cash == 0:
            return
        if deposit:
            self.portfolio.add_cash(float(cash))
        else:
            self.portfolio.withdraw_cash(float(cash))
        print("Transaction complete")

    def stock_interface(self):
        choice = input("Which stock do you wish to trade?  (enter 0 for main menu) ")
        if choice == 0:
            return
        if choice not in self.portfolio.market.stocks:
            print("Couldn't locate stock")
            return
        buy_input = input("Do you wish to buy or sell {0}? ".format(choice))
        if "buy" not in buy_input.lower() and "sell" not in buy_input.lower():
            return
        buy = True if "buy" in buy_input.lower() else False
        if not buy and choice not in self.portfolio.portfolio:
            print("You do not own any shares of {0}".format(choice))
            return
        quantity = input("How many shares do you wish to {0}? ".format("buy" if buy else "sell"))
        if buy:
            self.portfolio.buy_stock(choice, quantity)
        else:
            self.portfolio.sell_stock(choice, quantity)

    def exit(self):
        print("Thank you for visiting Python Portfolio")
        sys.exit(0)
