# Imports the Board class to create and print a new blank board
from board import Board
# Imports the necessary variables to be used to display the game
import start

def print_blank_and_user_boards():
    """
    Will print a blank board to represent the computer's ships,
    and print the user's board which was just created side by side.
    Will also print how many of each player's ships have sunk,
    and this will be updated throughout the game.
    """

    blank_board = Board(8)
    blank_board.create_board()
    blank_board.print_board()

print_blank_and_user_boards()