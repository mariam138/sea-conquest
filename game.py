# Allow terminal to be cleared when function is called
from clear import clear_terminal
# To use various random methods for the "computer" player
import random
# To create a board for the computer
from board import Board

# Place these into a main() later on
computer_board = Board(8)
computer_board.create_board()
computer_board.print_board()