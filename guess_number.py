#Code written by Salim O. Oyinlola

#Importing Libraries
import random
import os

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        
    
    print(f'Yay! Congrats, you have guessed the number {random_number} correctly!')


def computer_guess(y):
    your_number = int(input('Input a number between 1 and 10 for the computer to guess.'))
    computer_random_number = 0
    while computer_random_number != your_number:
        computer_random_number = random.randint(1,y)
        if computer_random_number < your_number:
            print(f'The computer guessed {computer_random_number}!')
            computer_random_number = random.randint(computer_random_number, y)
    
        elif computer_random_number > your_number:
            print(f'The computer guessed {computer_random_number}!')
            computer_random_number = random.randint(1, computer_random_number)

    print(f'Your number is {computer_random_number} !')


print('Pick a option!')
choice = int(input('Enter 1 if you want to guess a number and 2 if you want the computer to guess your name: '))
if choice == 1:
    guess(10)
    os.system("PAUSE")
elif choice == 2:
    computer_guess(10)
    os.system("PAUSE")