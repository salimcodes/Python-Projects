#Code written by Salim O. Oyinlola
import random
from words import words

#Function to ensure we get valid word

def get_valid_words(words):
    word = random.choice(words) #This randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()




#Twitter @kylieyying: https://twitter.com/SalimOpines
#Github: https://www.github.com/salimcodes
