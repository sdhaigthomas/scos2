from gameplay import GamePlay
from time import sleep
game = GamePlay()
###################################################################################################################################
game.fullPriceChanges(True)
while True:
    game.avgValue(game.doritos)
    game.HUD()
    if game.options() == "":
        game.fullPriceChanges(True)
        game.player.balance -= 40000
        if game.player.balance < 0:
            for i in game.log: print("Date of transaction:" , i.portfolio["date"], "| Name of share:",i.portfolio["name"], "| Transaction type:", i.portfolio["transType"], "| Shares involved in transaction:", i.portfolio["noShares"], "| Share price of share at time of purchase:", f'${i.portfolio["sharePrice"]/100:.2f}')
            exit("you ran out of money!")
        for i in range(10):
            sleep(0.5)
            game.HUD()
            game.fullPriceChanges(False)
    game.days += 1
###################################################################################################################################