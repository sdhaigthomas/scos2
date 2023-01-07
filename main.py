from gameplay import GamePlay
from time import sleep
from random import randint as rnd
game = GamePlay()
###################################################################################################################################
game.fullPriceChanges(True)
while True:
    game.avgValue(game.doritos)
    game.HUD()
    if game.options() == "":
        game.fullPriceChanges(True)
        for i in range(10):
            sleep(0.5)
            game.HUD()
            game.fullPriceChanges(False)
    charge = 40000 + rnd(-1000, 1000)
    game.player.balance -= charge
    if game.player.balance < 0:
        for i in game.log: print("Date of transaction:" , i.portfolio["date"], "| Name of share:",i.portfolio["name"], "| Transaction type:", i.portfolio["transType"], "| Shares involved in transaction:", i.portfolio["noShares"], "| Share price of share at time of purchase:", game.formatNum(i.portfolio["sharePrice"]))
        exit("You have ran out of money! After being charged " + str(game.formatNum(charge)) + "!")
    game.days += 1
###################################################################################################################################