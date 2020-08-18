from portfolio import Market
from menu import Menu

if __name__ == "__main__":
    mrkt = Market()
    mrkt.add_stock("ABCD", .7, 20.3)
    mrkt.add_stock("SWIF", .3, 81.2)
    mrkt.add_stock("FIWL", .1, 60.08)
    mrkt.add_stock("FBSL", .6, 15.3)
    mrkt.add_stock("QOQO", .9, 22.4)
    mrkt.add_stock("BNGP", .5, 79.61)
    mrkt.add_stock("GQPI", .6, 20.3)
    mrkt.add_stock("XAIW", .3, 22.93)
    mrkt.add_stock("FWQU", .5, 49.0)
    mrkt.add_stock("WURP", .2, 55.24)

    bal = 200

    m = Menu(mrkt, bal)
    m.run()
