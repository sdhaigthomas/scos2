from random import randint as rnd
print("test")# REMOVE THIS
###################################################################################################################################
class Shares:
    def __init__(self, name, bid, offer, vol, owned, sector):
        self.name = name
        self.bid = bid
        self.offer = offer
        self.vol = vol
        self.owned = owned
        self.sector = sector
###################################################################################################################################
    def stockPriceChange(self, vol, price):
        negitiveVol = vol * -1
        price += rnd(negitiveVol, vol)
        if price <= 1:
            price = 1
        return round(price, 2)
###################################################################################################################################
    def offerGenerator(self, price):
        price = price * 1.10
        return price
###################################################################################################################################