from gameplay import GamePlay
from time import sleep
game = GamePlay()
game.HUD()
game.buy()
while True:
    if game.options() == "":
        for i in range(10):
            sleep(0.5)
            game.fullPriceChanges()
            game.HUD()