

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cheddar = 0
        self.stilton = 0
        self.parmesan = 0
        
    def getName(self):
        return self.name