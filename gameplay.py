from player import Player
from shares import Shares
from portfolio import Portfolio
from time import sleep

class GamePlay:
    def __init__(self):
        self.stilton = Shares("Stilton plc", 120, 123, 2,"Cheese Manufacturer")
        self.stilton = Shares("Parmesan plc", 100, 103, 4,"Cheese Manufacturer")
        self.cheddar = Shares("Cheddar plc", 52, 56, 3,"Cheese Manufacturer")
        #self.portfolio = Portfolio()
        self.greet()

    def greet(self):
        print("Welcome to stocks!")
        name = input("Please Enter a Name:\n")
        self.player = Player(name, 10000)
        print("Welcome,", self.player.getName())
    
    def dsdf(self):
        for i in range(10):
            print(Shares.stockPriceChange(self.cheddar.vol, self.cheddar.bid))
            time.sleep(1)



