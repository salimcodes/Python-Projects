#Code written by Salim O. Oyinlola

import random
import os

def play():
    user = input("What is your choice; 'r' for rock, 'p' for paper, 's' for scissors! \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It is a tie!'

    #Given that r>s, s>p and p>r

    if is_win(user, computer):
        return 'You won!'
    else:
        return 'You lost!'

def is_win(player, opponent):
    #returns true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())

os.system("PAUSE")



#Twitter @SalimOpines: https://twitter.com/SalimOpines
#Github: https://www.github.com/salimcodes
