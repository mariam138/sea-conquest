# Allow terminal to be cleared when function is called
from clear import clear_terminal
# To use various random methods for the "computer" player
import random
# To create a board for the computer
from board import Board
# To create the different ships
from ships import Ships

# Place these into a main() later on
random_board = Board(8)
random_board.create_board()

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
    
    return computer_col


def random_row_coord(board):
    """
    Using the dimensions of the game board, a random number will
    be generated within that range using the random module.
    This will then be put into a variable representing the
    row. This method will be used both for placing the computers'
    ships and for guessing coordinates in game
    """
    computer_row = random.randrange(1, board.dimensions)
    return computer_row


def random_ship_dir():
    """
    A list containing the two choices of either "horizontal"
    or "vertical" will be used to randomly pick a direction
    for the computers' ships to be placed, using the random module.
    """
    directions = ["h", "v"]
    comp_ship_direction = random.choice(directions)
    return comp_ship_direction

def computer_place_ships(ship, board):
    """
    Uses similar method from Ships to place ships onto board.
    Using the functions created above, the "computer" will place
    its ships in random positions on the board. Similar validation
    for the user will be used to make sure the ships fit onto
    the board and do not overlap.
    """

    computer_ship_coords = []
    while True:
        row = random_row_coord(board)
        col = random_column_coord()
        direction = random_ship_dir()

        ship_fits = True

        if direction == "h":
            if (ship.length + col) > (board.dimensions + 1):
                continue
            else:
                # ship_fits = True
                for i in range(ship.length):
                    if board.board[row][col + i] != "~":
                        ship_fits = False
                        break
        elif direction == "v":
            if (ship.length + row) > (board.dimensions + 1):
                continue
            else:
                # ship_fits = True
                for i in range(ship.length):
                    if board.board[row + i][col] != "~":
                        ship_fits = False

        if ship_fits:
            if direction == "h":
                for i in range(ship.length):
                    board.board[row][col + i] = "S"
                    computer_ship_coords.append((row, col + i))
            elif direction == "v":
                for i in range(ship.length):
                    board.board[row + i][col] = "S"
                    computer_ship_coords.append((row + i, col))
            return board


battleship = Ships("Battleship", 4)
destroyer_one = Ships("Destroyer 1", 3)
destroyer_two = Ships("Destroyer 2", 3)
submarine_one = Ships("Submarine 1", 2)
submarine_two = Ships("Submarine 2", 2)
# Place each ship instance into a list for looping
player_ships = [
    battleship, destroyer_one, destroyer_two,
    submarine_one, submarine_two
]
all_comp_ship_coords = []

# Store created random board into variable called computer_board
# for game use
for ship in player_ships:
   computer_board = computer_place_ships(ship, random_board)
   all_comp_ship_coords.extend(computer_ship_coords)
print(all_comp_ship_coords)
