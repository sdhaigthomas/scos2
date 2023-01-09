from player import Player
from shares import Shares
from portfolio import Portfolio
from time import sleep
from os import system
from math import floor
import platform
###################################################################################################################################
class GamePlay:
    def __init__(self):
        self.portfolio = Portfolio("Startup", "Startup","Startup","Startup","Startup")
        self.os = 0
        self.oldOffers = []
        self.days = 0
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
        print(self.portfolio.averagePriceCalc(self.shareList, self.portfolio.log))
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
        msg = "You have " + self.formatNum(self.player.balance) + " | Would you like to, Buy[1], Sell[2], Wait Until Tomorrow[Enter] or Statistics[3]\n"
        choice = input(msg)
        if choice == "1" or choice == "2" or choice == "3" or choice == "":
            if choice == "": return choice
            else:
                choice = int(choice)
###################################################################################################################################                
                if choice == 1:
                    portfolioPreviewBuy = self.portfolioGen(self.buy())
                    if self.player.balance - portfolioPreviewBuy.portfolio["noShares"] * portfolioPreviewBuy.portfolio["sharePrice"] < 0: 
                        print("You cant afford that!")
                        sleep(2)
                    else: 
                        self.portfolio.log.append(portfolioPreviewBuy)
                        self.player.balance -= portfolioPreviewBuy.portfolio["noShares"] * portfolioPreviewBuy.portfolio["sharePrice"]
###################################################################################################################################
                elif choice == 2:
                    portfolioPreviewSell = self.portfolioGen(self.sell())
                    self.portfolio.log.append(portfolioPreviewSell)
                    self.player.balance += portfolioPreviewSell.portfolio["noShares"] * portfolioPreviewSell.portfolio["sharePrice"]
###################################################################################################################################
                elif choice == 3: 
                    for i in self.portfolio.log:
                        print("Date of transaction:" , i.portfolio["date"], "| Name of share:",i.portfolio["name"], "| Transaction type:", i.portfolio["transType"], "| Shares involved in transaction:", i.portfolio["noShares"], "| Share price of share at time of purchase:", self.formatNum(i.portfolio["sharePrice"]))
                    input("Press enter to continue.")
                else: pass
        else: input("Please enter a valid option | Press enter to continue")
###################################################################################################################################
    def buy(self):
        self.clear()
        return self.transactions("Buy", "buy")
###################################################################################################################################
    def sell(self):
        self.clear()
        return self.transactions("Sell", "sell")
###################################################################################################################################
    def portfolioGen(self, transactions): return Portfolio(self.days,   self.shareList[transactions[0]].name,   transactions[2],    transactions[1],   self.shareList[transactions[0]].offer)
                                            #                Days      |  Name of share                        |  Transaction Type  | Amount of shares | Offer
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
            if i.portfolio["name"] == shareName:
                if i.portfolio["transType"] == "buy": owned += i.portfolio["noShares"]
                else: owned -= i.portfolio["noShares"]
        return owned
###################################################################################################################################
    def avgValue(self, share):
        sharesLog = []
        holderList = []
        counter = 0
        for i in self.portfolio.log:
            if share.name == i.portfolio["name"]:
                if i.portfolio["transType"] == "buy": counter += i.portfolio["noShares"]
                else: counter -= i.portfolio["noShares"]    
                holderList = []
                toSave = ["noShares", "transType", "sharePrice"]
                for j in range(len(toSave)): holderList.append(i.portfolio[toSave[j]])
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