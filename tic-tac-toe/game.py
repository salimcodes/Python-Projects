import os
import math
import time
from player import HumanPlayer, ComputerPlayer

#from player import RandomComputerPlayer
class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)] #Since we will use a single list to rep 3x3 board
        self.current_winner = None #To keep track of winner!

   

    def print_board(self):
        #This is just getting the rows
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc {to tell what number corresponds to what box}
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. If invalid, then return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        
        # WINNER IF 3 IN A ROW ANYWHERE
        # checking the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True

        # checking the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True

        #checking the diagonals [but only if the square is an even number]
        # [0,2,4,6,8] are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diagonal
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True

        # If all these fail
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):
    #returns the winner of the game (the Letter)! or None for a tie

    if print_game:
        game.print_board_nums()

    letter = 'X' #Assuming X to be starting letter

    #Iterate while the game still has empty squares
    
    while game.empty_squares():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #Defining a function to make a move
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('') #just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            #after we made our move, we need to alternate letters

            letter = 'O' if letter == 'X' else 'X'  # switches player

        print('Loading...') 
        time.sleep(1) #Pausing for one second and adding "Loading..." tag to give realistic feel. 

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    choice = input("Do you want to play as 'X' or 'O'")
    if choice == 'O' or 'o':
        x_player = ComputerPlayer('X')
        o_player = HumanPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player, print_game=True)
   

    elif choice == 'X' or 'x':
        x_player = HumanPlayer('X')
        o_player = ComputerPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player, print_game=True)
    
os.system("PAUSE")


#Twitter @SalimOpines: https://twitter.com/SalimOpines
#Github: https://www.github.com/salimcodes


