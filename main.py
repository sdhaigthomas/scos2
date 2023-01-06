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
        for i in range(10):
            sleep(0.5)
            game.HUD()
            game.fullPriceChanges(False)
    game.days += 1
###################################################################################################################################