from player import Player
from shares import Shares
from portfolio import Portfolio
from time import sleep
from os import system
from datetime import datetime

###################################################################################################################################
class GamePlay:
    def __init__(self):
        self.clear()
        self.stilton = Shares("Stilton Plc", 152550, 153070, 12100, 0,"Cheese Manufacturer")
        self.parmesan = Shares("Parmesan Plc", 52320, 10323, 400, 0,"Cheese Manufacturer")
        self.cheddar = Shares("Cheddar Plc", 15230, 15350, 100, 0,"Cheese Manufacturer")
        self.blueCheese = Shares("doritos Plc", 10, 13, 100, 0,"Cheese Manufacturer")
        self.shareList = [self.stilton, self.parmesan, self.cheddar, self.blueCheese]
        self.log = []
        self.oldOffers = []
        self.days = 0
        self.greet()
        self.fullPriceChanges()
###################################################################################################################################
    def fullPriceChanges(self):
        oldOffers = []
        for i in self.shareList:
            oldOffers.append(int(i.offer))
        for i in self.shareList:
            i.bid = i.stockPriceChange(i.vol, i.bid)
            i.offer = i.bid
            i.offer += i.offerGenerator(i.vol)
        self.oldOffers = oldOffers
###################################################################################################################################
    def greet(self):
        print("Welcome to stocks!")
        name = input("Please Enter a Name:\n")
        self.player = Player(name, 1000000)
        print("Welcome,", self.player.getName())
###################################################################################################################################
    def HUD(self):
        self.clear()
        self.lines()
        diffCounter = 0
        for i in self.shareList:
            difference = abs(self.oldOffers[diffCounter] - i.offer)
            if i.offer < self.oldOffers[diffCounter]: plusMinus = "-"
            else: plusMinus = "+"
            print(i.name + ": Bid:", f'${i.bid/100:,.2f}',"| Offer:", f'${i.offer/100:,.2f}',"(" + plusMinus + str(round(difference, 2) / 100) + ") | Vol:" , i.vol/100, "| Amount Owned", self.aggregator(i.name))
            diffCounter += 1
        self.lines()
###################################################################################################################################
    def options(self):
        msg = "You have " + f'${self.player.balance/100:,.2f}' + "| Would you like to, Buy[1], Sell[2], Wait Until Tomorrow[Enter] or Statistics[3]\n"
        choice = input(msg)
        if choice == "1" or choice == "2" or choice == "3" or choice == "":
            if choice == "":
                return choice
            else:
                choice = int(choice)
                if choice == 1:
                    portpofioPreview = self.portfolioGen(self.buy())
                    if self.player.balance - portpofioPreview.portfolio["noShares"] * portpofioPreview.portfolio["sharePrice"] < 0: 
                        print("You cant afford that!")
                        sleep(2)
                    else: 
                        self.log.append(self.portfolioGen(self.buy()))
                        self.player.balance -= portpofioPreview.portfolio["noShares"] * portpofioPreview.portfolio["sharePrice"]
                if choice == 2: 
                    self.log.append(self.portfolioGen(self.sell()))
                    self.player.balance += portpofioPreview.portfolio["noShares"] * portpofioPreview.portfolio["sharePrice"]
                if choice == 3: 
                    for i in self.log:
                        print("Date of transaction:" , i.portfolio["date"], "| Name of share:",i.portfolio["name"], "| Transaction type:", i.portfolio["transType"], "| Shares involved in transaction:", i.portfolio["noShares"], "| Share price of share at time of purchase:", f'${i.portfolio["sharePrice"]/100:.2f}')
                    input("Press enter to continue.")
                else: pass
        else: print("Please enter a valid option.")
###################################################################################################################################
    def buy(self):
        self.clear()
        return self.transactions("Buy", "buy")
###################################################################################################################################
    def sell(self):
        self.clear()
        return self.transactions("Sell", "sell")
###################################################################################################################################
    def portfolioGen(self, transactions):
        return Portfolio(self.days, self.shareList[transactions[0]].name, transactions[2], transactions[1], self.shareList[transactions[0]].offer)
###################################################################################################################################
    def transactions(self, transTypeCaps, transType):
        lenShareList = len(self.shareList)
        self.lines()
        print(transTypeCaps)
        for i in range(lenShareList): print("Name:",self.shareList[i].name,"| Owned", self.aggregator(self.shareList[i].name),"Press", i + 1, "to " + transType + ".")
        self.lines()
        which = self.integerValidator(1, lenShareList, "What share would you like to " + transType + "?") - 1
        amount = self.integerValidator(1, 214483647, "How many would you like to " + transType + "?")
        return which, amount, transType
###################################################################################################################################
    def integerValidator(self, minimum, maximum, message):
        while True:
            num = input(message + " | Press Enter to cancel.\n")
            if num == "": 
                return 0
            try:
                num = int(num)
                if num < maximum or num == maximum or num < minimum:
                    return num
                else:
                    print("Please enter a valid number within 1 and " + str(maximum) + ".")
            except:
                print("Please enter a number.") 
###################################################################################################################################
    def aggregator(self, shareName):
        owned = 0
        for i in self.log:
            if i.portfolio["name"] == shareName:
                if i.portfolio["transType"] == "buy":
                    owned += i.portfolio["noShares"]
                else:
                    owned -= i.portfolio["noShares"]
        return owned
###################################################################################################################################
    def lines(self): print("----------------------------------")
###################################################################################################################################
    def clear(self): system("clear")
###################################################################################################################################     