###################################################################################################################################
class Main:
    def __init__(self):
        instructions = self.questions()
        self.instructions(instructions[0],instructions[1],instructions[2],instructions[3],instructions[4],instructions[5],instructions[6])
 ###################################################################################################################################       
    def integerValidator(self,minimum, maximum, message):
        while True:
            num = input(message)
            if num == "": return False
            try:
                num = int(num)
                if num < maximum or num == maximum or num < minimum:return num
                else:print("Please enter a valid number within 1 and " + str(maximum) + ".")  
            except:print("Please enter a number.") 
###################################################################################################################################
    def offerGenerator(self, price):
            price = price * 1.10
            return price
###################################################################################################################################
    def questions(self):
        comps = []
        name = input("What would you like to name the company?\n")
        varName = input("Give the share a short name, not includeing spaces, caps, punctuation or special charicterss\n")
        bid = self.integerValidator(1, 1000000000, "What should " + name + "'s bid start as(In $)?\n") * 100
        offer = self.offerGenerator(bid)
        vol = self.integerValidator(1, 1000000000, "What should " + name + "'s volitility be(In $)?\n")
        owned = 0
        sectorChoice = self.integerValidator(1, 4, "What sector is " + name + " in?\nDigital[1]\nManufacture[2]\nBanking[3]\nRetail[4]\n")
        if sectorChoice == 1: sector = "digital"
        elif sectorChoice == 2: sector = "manufacture"
        elif sectorChoice == 3: sector = "banking"
        elif sectorChoice == 4: sector = "retail"
        spaceName = name
        if len(name) < 17:
            for i in range(17 - len(name)): spaceName += " "
                
        return varName, bid, offer, vol, owned, sector, spaceName
###################################################################################################################################
    def instructions(self, varName, bid, offer, vol, owned, sector, spaceName):
        print("Copy the code below and add to gameplays.py's constructor (Ctrl+f 'def __init__(self):'). In the constructor you will find #INSERT CUSTOM COMPANYS HERE paste data below. ")
        final = "self."+ varName +" = " "Shares('" + str(spaceName) + "'," + str(bid) + "," + str(offer) + "," + str(vol) + "," + str(owned) + ",'" + str(sector) + "')"
        print(final)
        print("When you have done that find 'self.shareList' you can use Ctrl+F. Find the end of the list(remember to exclude the close ]) add a comma and paste text below")
        print("self."+ varName)
###################################################################################################################################hi
main = Main()