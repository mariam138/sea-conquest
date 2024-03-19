# Allow terminal to be cleared when function is called
from clear import clear_terminal
# To use various random methods for the "computer" player
import random
# To create a board for the computer
from board import Board

# Place these into a main() later on
computer_board = Board(8)
# computer_board.create_board()
# computer_board.print_board()

def random_column_coord():
    """
    A dictionary will be again defined for each letter
    coordinate as its corresponding index number. A
    list will then be made containing the letter choices which
    will be chosen as random as the column coordinate. The letter
    will be chosen using the built-in random module.
    """
    letter_coord_dict = {
        "A": 1, "B": 2, "C": 3, "D" : 4, "E": 5, "F": 6, "G": 7, "H": 8
    }
    letter_choices = ["A", "B", "C", "D", "E", "F", "G", "H"]
    computer_col_coord = random.choice(letter_choices)
    if computer_col_coord in letter_coord_dict:
                computer_col = letter_coord_dict[computer_col_coord]
    print(computer_col)


def random_row_coord(board):
    """
    Using the dimensions of the game board, a random number will
    be generated within that range using the random module.
    This will then be put into a variable representing the
    row. This method will be used both for placing the computers'
    ships and for guessing coordinates in game
    """
    computer_row = random.randrange(1, board.dimensions)
    print(computer_row)


def random_ship_dir():
    """
    A list containing the two choices of either "horizontal"
    or "vertical" will be used to randomly pick a direction
    for the computers' ships to be placed, using the random module.
    """
    directions = ["h", "v"]
    comp_ship_direction = random.choice(directions)
    print(comp_ship_direction)

def computer_place_ships(board):
    """
    Uses similar method from Ships to place ships onto board.
    The random module will be used to give a random column
    and random row, a choice between horizontal and vertical
    placement and use the same validation to make sure the ships fit onto the board and do not overlap.
    """
    # Stores directions which ships can be placed
    # Into a list so that a random choice between the two
    # Can be chosen for random ship placement by the "computer"

    # while True:
    #     col = board.convert_coord_to_index()
    #     row = board.validate_number_coord()
    #     print("Which direction do you want your ship to be placed?")
    #     print("Type 'h' for horizontal or 'v' for vertical.")
    #     direction = input("Please enter 'h' or 'v':\n")
    #     if direction != "h" and direction != "v":
    #         print("That is not a valid input. Please try again.")
    #     elif direction == "h":
    #         if (self.length + col) > (board.dimensions + 1):
    #             print("The ship doesn't fit. Please try again.")
    #             continue
    #         else:
    #             for i in range(self.length):
    #                 if board.board[row][col + i] != "~":
    #                     print("The ship overlaps with another", end=" ")
    #                     print("ship. Please try again.")
    #                     break
    #                 else:
    #                     for i in range(self.length):
    #                         board.board[row][col + i] = "S"
    #                         self.ship_coords.append((row, col + i))
    #                 clear_terminal()
    #                 board.print_board()
    #                 return board
    #     elif direction == "v":
    #         if (self.length + row) > (board.dimensions + 1):
    #             print("The ship doesn't fit. Please try again.")
    #             continue
    #         else:
    #             for i in range(self.length):
    #                 if board.board[row + i][col] != "~":
    #                     print("The ship overlaps with another", end=" ")
    #                     print("ship. Please try again.")
    #                     break
    #                 else:
    #                     for i in range(self.length):
    #                         board.board[row + i][col] = "S"
    #                         self.ship_coords.append((row + i, col))
    #                 clear_terminal()
    #                 board.print_board()
    #                 return board

# computer_place_ships(computer_board)
random_column_coord()
random_row_coord(computer_board)
random_ship_dir()
