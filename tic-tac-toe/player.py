import os
import math
import random


class Player:
    def __init__(self, letter):
        #Letter can be X or O
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass

os.system("PAUSE")

#Twitter @SalimOpines: https://twitter.com/SalimOpines
#Github: https://www.github.com/salimcodes