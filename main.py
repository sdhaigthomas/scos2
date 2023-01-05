from gameplay import GamePlay
from time import sleep
game = GamePlay()
###################################################################################################################################
while True:
    game.HUD(game.fullPriceChanges())
    if game.options() == "":
        for i in range(10):
            sleep(0.5)
            game.HUD(game.fullPriceChanges())
    game.days += 1
###################################################################################################################################