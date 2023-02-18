from player import Player
from random import randint as rnd
from shares import Shares
from portfolio import Portfolio
from time import sleep
from os import system
from math import floor
import platform
###################################################################################################################################
class GamePlay:
    def __init__(self):
        self.portfolio = Portfolio()
        self.os = 0
        self.days = 0
        self.charge = 0
        self.oldOffers = []
        self.thomasIndustrial = Shares("Thomas Industrial", 152550, 153070, 12100, 0,"manufacturere")
        self.alexAndSons = Shares("Alex & Sons      ", 52320, 10323, 400, 0,"legal")
        self.Edht2 = Shares("Edht2 Websevices ", 15230, 15350, 100, 0,"digtal")
        self.sdhtMedia = Shares("Sdht Media       ", 10, 13, 100, 0,"digital")
        self.diamondBank = Shares("Diamond Bank     ", 2500023, 2523212, 100000, 0, "bank")
        #INSERT CUSTOM COMPANYS HERE
        self.shareList = [self.diamondBank, self.thomasIndustrial,self.alexAndSons, self.Edht2, self.sdhtMedia]
        self.greet()
        self.fullPriceChanges(True)
###################################################################################################################################
    def stats(self):
        if self.player.balance < 0:
            for i in self.log: print("Date of transaction:" , i["date"], "| Name of share:",i["name"], "| Transaction type:", i["transType"], "| Shares involved in transaction:", i["noShares"], "| Share price of share at time of purchase:", game.formatNum(i["sharePrice"]))
            exit("You have ran out of money! You survived " + str(self.days) + " and whent bankrupt after being charged " + str(self.formatNum(self.charge)) + "!")
###################################################################################################################################
    def chargePlayer(self):
        self.charge = 40000 + rnd(-1000, 1000)
        self.player.balance -= self.charge
###################################################################################################################################
    def fullPriceChanges(self, isFirst):
        oldOffers = []
        if isFirst == True:
            for i in self.shareList:
                oldOffers.append(int(i.offer))
            self.oldOffers = oldOffers
        for i in self.shareList:
            i.bid = i.stockPriceChange(i.vol, i.bid)
            i.offer = i.bid
            i.offer += i.offerGenerator(i.vol)
###################################################################################################################################
    def greet(self):
        print("Welcome to stocks!")
        name = input("Please Enter a Name:\n")
        self.player = Player(name, 1000000)
        print("Welcome,", self.player.getName())
        self.os = platform.system()
###################################################################################################################################
    def HUD(self):
        self.clear()
        self.lines()
        diffCounter = 0
        for i in self.shareList:
            difference = abs(self.oldOffers[diffCounter] - i.offer)
            if i.offer < self.oldOffers[diffCounter]: plusMinus = "-"
            else: plusMinus = "+"
            print(i.name + ": Bid:", self.formatNum(i.bid)," | Offer:", self.formatNum(i.offer),"(" + plusMinus + str(round(difference, 2) / 100) + ") | Vol:" , i.vol/100, "| Amount Owned", self.aggregator(i.name))
            diffCounter += 1
        self.lines()
###################################################################################################################################
    def formatNum(self, num): return f'${num/100:,.2f}'   
###################################################################################################################################
    def options(self):
        msg = "You have " + self.formatNum(self.player.balance) + " | Would you like to: Buy[1], Sell[2], View Portfolio[3], Statistics[4], Wait Until Tomorrow[Enter] |\n"
        choice = input(msg)
        if choice in {"1","2","3","4",""}:
            if choice == "": return choice
            else:
                choice = int(choice)              
                if choice == 1:
                    portfolioPreviewBuy = self.portfolioGen(self.buy())
                    if self.player.balance - portfolioPreviewBuy["noShares"] * portfolioPreviewBuy["sharePrice"] < 0: 
                        print("You cant afford that!")
                        sleep(2)
                    else: 
                        self.portfolio.log.append(portfolioPreviewBuy)
                        self.player.balance -= portfolioPreviewBuy["noShares"] * portfolioPreviewBuy["sharePrice"]
                elif choice == 2:
                    portfolioPreviewSell = self.portfolioGen(self.sell())
                    self.portfolio.log.append(portfolioPreviewSell)
                    self.player.balance += portfolioPreviewSell["noShares"] * portfolioPreviewSell["sharePrice"]
                elif choice == 3:
                    for i in self.shareList:
                        print("You Own: " + str(self.aggregator(i)) + " shares in  " + str(i.name))
                    input("Press enter to continue.")
                elif choice == 4: 
                    for i in self.portfolio.log:
                        print("Date of transaction:" , i["date"], "| Name of share:",i["name"], "| Transaction type:", i["transType"], "| Shares involved in transaction:", i["noShares"], "| Share price of share at time of purchase:", self.formatNum(i["sharePrice"]))
                    input("Press enter to continue\n")
                    #print(self.portfolio.averagePriceCalc(self.shareList, self.portfolio.log))
                    self.stats()
                else: pass
        else: input("Please enter a valid option | Press enter to continue\n")
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
        portfolio = {"date" : self.days, "name" : self.shareList[transactions[0]].name, "transType": transactions[2], "noShares" :  transactions[1], "sharePrice" : self.shareList[transactions[0]].offer}
        return portfolio
###################################################################################################################################
    def transactions(self, transTypeCaps, transType):
        lenShareList = len(self.shareList)
        self.lines()
        print(transTypeCaps)
        msg = ""
        for i in range(lenShareList): 
            if transType == "buy": msg = str("| You can afford " + str(floor(self.player.balance / self.shareList[i].offer)))
            print("Name:",self.shareList[i].name,"| Owned", self.aggregator(self.shareList[i].name),"| Offer:",self.formatNum(self.shareList[i].offer), msg,"| Press", i + 1, "to " + transType + ".")
        self.lines()
        which = self.integerValidator(1, lenShareList, "What share would you like to " + transType + "?", True) - 1
        amount = self.integerValidator(1, 214483647, "How many would you like to " + transType + "?", True)
        return which, amount, transType
###################################################################################################################################
    def integerValidator(self, minimum, maximum, message, forBuySell):
        if forBuySell == True: msg = "You have: " + str(self.formatNum(self.player.balance)) + " | " + message + " | Press Enter to cancel.\n"
        else: msg = message + " | Press Enter to cancel.\n"
        while True:
            num = input(msg)
            if num == "": return False
            try:
                num = int(num)
                if num < maximum or num == maximum or num < minimum:return num
                else:print("Please enter a valid number within 1 and " + str(maximum) + ".")  
            except:print("Please enter a number.") 
###################################################################################################################################
    def aggregator(self, shareName):
        owned = 0
        for i in self.portfolio.log:
            if i["name"] == shareName:
                if i["transType"] == "buy": owned += i["noShares"]
                else: owned -= i["noShares"]
        return owned
###################################################################################################################################
    def avgValue(self, share):
        sharesLog = []
        holderList = []
        counter = 0
        for i in self.portfolio.log:
            if share.name == i["name"]:
                if i["transType"] == "buy": counter += i["noShares"]
                else: counter -= i["noShares"]    
                holderList = []
                toSave = ["noShares", "transType", "sharePrice"]
                for j in range(len(toSave)): holderList.append(i[toSave[j]])
                sharesLog.append(holderList)
                if counter == 0:
                    sharesLog = []
        print(sharesLog)
        print(counter)
###################################################################################################################################
    def lines(self): print("----------------------------------")
###################################################################################################################################
    def clear(self): 
        if self.os == "Windows": system("cls")
        else: system("clear")
###################################################################################################################################     