from random import randint as rnd
class Shares:
    def __init__(self, name, bid, offer, vol, sector):
        self.name = name
        self.bid = bid
        self.offer = offer
        self.vol = vol
        self.sector = sector

    def stockPriceChange(vol, price):
        price += rnd(vol * -1, vol)
        return price
    def offerGenorator(self, price):
        price += rnd(1,2)
        return price
        