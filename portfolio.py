###################################################################################################################################
class Portfolio:
    def __init__(self, date, name, transType, noShares, sharePrice):
        self.portfolio = {"date" : date, "name" : name, "transType": transType, "noShares" : noShares, "sharePrice" : sharePrice}
        self.log = []
###################################################################################################################################
    def pAndL():
        pass # print total profit and loss#
###################################################################################################################################
    def listPortfolio():
        pass
###################################################################################################################################
    def averagePriceCalc(self, shareList, log):
            for share in shareList:
                count = 0
                cmlt = 0  # count minus last transaction
                trans_log = []
                trans = []
                message = ''
                for tr in log:
                    if tr.portfolio["name"] == share.name:
                        lt = tr.portfolio["noShares"]

                        if  tr.portfolio["transType"] == "buy":  
                            cmlt = count
                            count += lt

                        elif tr.portfolio["transType"] == "sell":
                            cmlt = count
                            count -= lt
                        if cmlt >= 0 and count > cmlt or cmlt <= 0 and count < cmlt: # if square or net long/short and a purchase/sale is made ...
                            trans = [tr.portfolio["noShares"], tr.portfolio["sharePrice"]]
                            trans_log.append(trans)
                            message = 'net long/short and a purchase/sale has been made. ' + tr.portfolio["name"]
                        elif cmlt > 0 and count < 0 or cmlt < 0 and count > 0: # if new transaction reverses the long/short position into a short/long position...
                            trans_log = []
                            trans = [count, tr.portfolio["sharePrice"]]
                            trans_log.append(trans)
                            message = 'new transaction reverses the long/short position into a short/long position. ' + tr.portfolio["name"]
                        elif count == 0: # position is 0
                            trans_log = []
                            trans = []
                            message = 'position is 0' + tr.portfolio["name"]
                        else: # player is long / short and a sale/purchase has been made not sufficient to reverse the position. Do nothing
                            message = 'player is long / short and a sale/purchase has been made not sufficient to reverse the position. Do nothing'
                        print(f"{tr.portfolio['name']}. Trans_log = {trans_log}\nTrans = {trans}\n")
                        print(message)
