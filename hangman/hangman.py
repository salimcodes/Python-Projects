#Code written by Salim O. Oyinlola
import random
from words import words
import string
import os

#Function to ensure we get valid word

def get_valid_words(words):
    word = random.choice(words) #This randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)            #Letters in the randomly chosen word
    alphabet = set(string.ascii_uppercase)      #All letters in the English alphabets
    used_letters = set()        #The letters the users has guessed

    lives = 10
    #Getting the user's input 
    while len(word_letters) > 0 and lives > 0:
        #print()
        print('You have ',lives,'lives left! You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))


        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter is not in word')
        elif user_letter in used_letters:
            print('You have already used that character. Kindly try again!')

        else:
            print('Invalid character. Please try again!')
      
    if lives == 0:
        print('My apologies. You died! \n The word was ',word)
    else:
        print('You guessed the word', word,'!!')
hangman()
os.system("PAUSE")

#Twitter @SalimOpines: https://twitter.com/SalimOpines
#Github: https://www.github.com/salimcodes
