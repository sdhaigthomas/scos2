from os import system
def integerValidator(minimum, maximum, message):
    while True:
        num = input(message)
        if num == "": return False
        try:
            num = int(num)
            if num < maximum or num == maximum or num < minimum:return num
            else:print("Please enter a valid number within 1 and " + str(maximum) + ".")  
        except:print("Please enter a number.") 
def offerGenerator(price):
        price = price * 1.10
        return price
comps = 0
while True:
    name = input("What would you like to name the company?\n")
    bid = integerValidator(1, 1000000000, "What should " + name + "'s bid start as(In $)?\n") * 100
    offer = offerGenerator(bid)
    vol = integerValidator(1, 1000000000, "What should " + name + "'s volitility be(In $)?\n")
    owned = 0
    sectorChoice = integerValidator(1, 4, "What sector is " + name + " in?\nDigital[1]\nManufacture[2]\nBanking[3]\nRetail[4]")
    if sectorChoice == 1: sector = "digital"
    elif sectorChoice == 2: sector = "manufacture"
    elif sectorChoice == 3: sector = "banking"
    elif sectorChoice == 4: sector = "retail"
    if len(name) < 10:
        for i in 10 - len(name):
            name += " "
    comps += 1
    repeat = integerValidator(1,2,"Do you want to make another new company(Yes[1], No[2])?")
    if repeat == 2: break