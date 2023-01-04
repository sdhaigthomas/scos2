from player import Player
from shares import Shares
from portfolio import Portfolio
from time import sleep
from os import system
###################################################################################################################################
class GamePlay:
    def __init__(self):
        self.stilton = Shares("Stilton Plc", 152550, 153070, 2100, 0,"Cheese Manufacturer")
        self.parmesan = Shares("Parmesan Plc", 52320, 10323, 400, 0,"Cheese Manufacturer")
        self.cheddar = Shares("Cheddar Plc", 15230, 15350, 100, 0,"Cheese Manufacturer")
        self.blueCheese = Shares("doritos Plc", 10, 13, 100, 0,"Cheese Manufacturer")
        self.shareList = [self.stilton, self.parmesan, self.cheddar, self.blueCheese]
        self.greet()
###################################################################################################################################
    def fullPriceChanges(self):
        for i in self.shareList:
            i.bid = i.stockPriceChange(i.vol, i.bid)
            i.offer = i.bid
            i.offer += i.offerGenerator(i.vol)
###################################################################################################################################
    def greet(self):
        print("Welcome to stocks!")
        name = input("Please Enter a Name:\n")
        self.player = Player(name, 10000)
        print("Welcome,", self.player.getName())
###################################################################################################################################
    def HUD(self):
        self.clear()
        self.lines()
        for i in self.shareList: print(i.name + ": Bid:", f'${i.bid/100:.2f}',"| Offer:", f'${i.offer/100:.2f}',"| Vol:" , i.vol/100)
        self.lines()
    def sharesOwned(self):
        pass
###################################################################################################################################
    def options(self):
        choice = input("Would you like to, Buy[1], Sell[2], Wait Until Tomorrow[Enter] or Statistics[3]\n")
        if choice == "1" or choice == "2" or choice == "3" or choice == "":
            if choice == "":
                return choice
            else:
                choice = int(choice)
                if choice == 1: self.buy()
                if choice == 2: self.sell()
                if choice == 3: pass #Stats 
                else:pass
        else: print("Please enter a valid option.")
###################################################################################################################################
    def buy(self):
        transactions = self.transactions("Buy", "buy")
        return transactions[0], transactions[1], transactions[2]
###################################################################################################################################
    def sell(self):
        transactions = self.transactions("Sell", "sell")
        return transactions[0], transactions[1], transactions[2]
############################################################################################################
    def transactions(self, transTypeCaps, transType):
        counter = 0
        toSell = None
        lenShareList = len(self.shareList)
        self.lines()
        print(transTypeCaps)
        for i in range(lenShareList): print("Name:",self.shareList[i].name,"| Owned", self.shareList[i].owned,"Press", i + 1, "to " + transType + ".")
        self.lines()
        num = self.integerValidator(1, lenShareList, "What share would you like to " + transType + "?") - 1
        amount = self.integerValidator(1, 214483647, "How many would you like to " + transType + "?")
        return num, amount, transType
############################################################################################################
    def integerValidator(self, minimum, maximum, message):
        while True:
            num = input(message + " | Press Enter to cancel.\n")
            if num == "": 
                return 0
            try:
                num = int(num)
                if num < maximum or num < minimum:
                    return num
                else:
                    print("Please enter a valid number within 1 and " + str(maximum) + ".")
            except:
                print("Please enter a number.") 
###################################################################################################################################
    def lines(self): print("----------------------------------")
###################################################################################################################################
    def clear(self): pass#system("clear")
###################################################################################################################################
        