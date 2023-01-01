from player import Player
from shares import Shares
from portfolio import Portfolio
from time import sleep
from os import system
class GamePlay:
    def __init__(self):
        self.stilton = Shares("Stilton Plc", 152550, 153070, 2100,"Cheese Manufacturer")
        self.parmesan = Shares("Parmesan Plc", 52320, 10323, 400,"Cheese Manufacturer")
        self.cheddar = Shares("Cheddar Plc", 15230, 15350, 100,"Cheese Manufacturer")
        self.blueCheese = Shares("Blue Cheese(uhgh) Plc", 10, 13, 100,"Cheese Manufacturer")
        self.shareList = [self.stilton, self.parmesan, self.cheddar, self.blueCheese]
        self.greet()
    def fullPriceChanges(self):
        for i in self.shareList:
            i.bid = i.stockPriceChange(i.vol, i.bid)
            i.offer = i.bid
            i.offer += i.offerGenerator(i.vol)
    def greet(self):
        print("Welcome to stocks!")
        name = input("Please Enter a Name:\n")
        self.player = Player(name, 10000)
        print("Welcome,", self.player.getName())
    def lines(self):print("----------------------------------")
    def HUD(self):
        system('clear')
        self.lines()
        for i in self.shareList: print(i.name + ": Bid:", f'${i.bid/100:.2f}',"| Offer:", f'${i.offer/100:.2f}',"| Vol:" , i.vol/100)
        self.lines()
    def options(self):
        choice = input("Would you like to, Buy[1], Sell[2], Wait Until Tomorrow[Enter] or Statistics[3]\n")
        if choice == "1" or choice == "2" or choice == "3" or choice == "":
            if choice == "":
                return choice
            else:
                choice = int(choice)
                if choice == 1: pass #Buy
                if choice == 2: pass #Sell
                if choice == 3: pass #Stats 
                else:pass
        else: print("Please enter a valid option.")
    def buy(self):
        counter = 1
        self.lines()
        print("                  BUY")
        for i in self.shareList:
            print("Name:",i.name,"|","Press", counter, "to buy.")
            counter += 1
        min_counter = 1 # user input validation requirement
        max_counter = counter # user input validation requirement
        self.lines()
        toBuy = input("What share would you like to buy?\n")
        