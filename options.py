###################################################################################################################################             
class Options:
    def buy(self):
        portfolioPreviewBuy = self.portfolioGen(self.buy())
        if self.player.balance - portfolioPreviewBuy["noShares"] * portfolioPreviewBuy["sharePrice"] < 0: 
            print("You cant afford that!")
            sleep(2)
        else: 
            self.portfolio.log.append(portfolioPreviewBuy)
            self.player.balance -= portfolioPreviewBuy["noShares"] * portfolioPreviewBuy["sharePrice"]
    def sell(self):
        portfolioPreviewSell = self.portfolioGen(self.sell())
        self.portfolio.log.append(portfolioPreviewSell)
        self.player.balance += portfolioPreviewSell["noShares"] * portfolioPreviewSell["sharePrice"]
    def portfolio(self):
        for i in self.shareList:
            print("You Own: " + str(self.aggregator(i)) + " shares in  " + str(i.name))
        input("Press enter to continue.")
    def statistics(self):
        for i in self.portfolio.log:
                print("Date of transaction:" , i["date"], "| Name of share:",i["name"], "| Transaction type:", i["transType"], "| Shares involved in transaction:", i["noShares"], "| Share price of share at time of purchase:", self.formatNum(i["sharePrice"]))
        input("Press enter to continue\n")
        #print(self.portfolio.averagePriceCalc(self.shareList, self.portfolio.log))
        self.stats()
###################################################################################################################################  