from player import Player
from shares import Shares
from portfolio import Portfolio
from time import sleep



class GamePlay:
    def __init__(self):
        self.stilton = Shares("Stilton plc", 120, 123, 2,"Cheese Manufacturer")
        self.parmesan = Shares("Parmesan plc", 100, 103, 4,"Cheese Manufacturer")
        self.cheddar = Shares("Cheddar plc", 52, 56, 11,"Cheese Manufacturer")
        self.greet()

    def greet(self):
        print("Welcome to stocks!")
        name = input("Please Enter a Name:\n")
        self.player = Player(name, 10000)
        print("Welcome,", self.player.getName())

    def HUD(self):
        print("----------------------------------")
        print("Cheddar: Bid", self.cheddar.bid,"| Offer:", self.cheddar.offer,"| Vol:", self.cheddar.vol)
        print("Stilton: Bid", self.stilton.bid,"| Offer:", self.stilton.offer,"| Vol:", self.stilton.vol)
        print("Parmesan: Bid", self.parmesan.bid,"| Offer:", self.parmesan.offer,"| Vol:", self.parmesan.vol)
        print("----------------------------------")
        choice = input("Would you like to, Buy[1], Sell[2], Wait Until Tomorrow[Enter] or Statistics[3]")
        try:
            choice = str(choice)
        except:
            print("Please enter a valid option.")

"""
    def testMethod(self):
        for i in range(100):
            print(Shares.stockPriceChange(self.cheddar.vol, self.cheddar.bid))
            self.cheddar.offer = self.cheddar.offerGenorator(self.cheddar.bid)
            sleep(1)
"""


