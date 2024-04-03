# Imports Board class from board.py module
from board import Board
# Imports function to clear the terminal from the clear module
from clear import clear_terminal
# Allows printing in colour to the terminal
from rich import print
# Allows delays before executing code
import time


class Ships:
    """
    Predefines the number of ships the player and computer gets.
    Each ship has a predefined length:
    1 x Battleship (length = 4)
    2 x Destroyer (length = 3)
    2 x Submarine (length = 2)
    Each ship also has a health which corresponds to their length,
    and also will have their own colours for printing purposes.
    """
    def __init__(self, name, length, colour, health):
        self.name = name
        self.length = length
        self.colour = colour
        self.health = length
        # Empty dictionary which the ship's coordinates will be stored
        # once placed on the board
        self.ship_coords = {}

    def print_ship_information(self):
        """
        Sets the length of each type of ship in a dictionary.
        Using the dictionary, this method will print out
        each type of ship and the length that each are. It will
        also tell the user how many of each type of ship they have.
        """
        # Defines each ship length in a dictionary to be used in other methods
        ship_length = {
            "Battleship": 4,
            "Destroyer": 3,
            "Submarine": 2
        }

        # Stores the keys and values into separate lists
        ship_names = ship_length.keys()
        ship_lengths = ship_length.values()

        print("You will have 1 Battleship, 2 Destroyers and 2 Submarines.\n")
        # Allows looping over two lists at the same time
        # To print the name and length of each ship
        for name, length in zip(ship_names, ship_lengths):
            print(f"The {name} has a length of {length}.")
        print("\n")

    def player_place_ships(self, board):
        """ The player will be asked to choose
        starting coordinates for their ship to be placed.
        Player will be asked if they want their ship horizontally
        or vertically. Validation will be done before a ship
        is placed to ensure it fits on the board and doesn't
        overlap with other ships placed.
        """

        print("You will now place your ships.")
        # While loop which will only be broken once validation passes
        while True:
            print(f"Placing [dodger_blue3]{self.name}....\n")
            print("Please enter your starting co-ordinate")
            # Stores the board methods into variables to use in the loop
            col = board.convert_coord_to_index()
            row = board.validate_number_coord()
            print("Which direction do you want your ship to be placed?")
            print("Type 'h' for horizontal or 'v' for vertical.")
            # Validation for the ship direction
            direction = input("Please enter 'h' or 'v':\n")
            if direction != "h" and direction != "v":
                print("Invalid direction. Please try again.")
            elif direction == "h":
                # If the length of the ship + the column number exceeds
                # The board dimensions, the player will be asked to try again
                if (self.length + col) > (board.dimensions + 1):
                    print("The ship doesn't fit. Please try again.")
                    time.sleep(2)
                    clear_terminal()
                    # Reprints out the current board once terminal is cleared
                    board.print_board()
                    continue
                else:
                    # Creates empty list to append the ships coordinates into
                    ship_coords = []
                    # Creates a flag to use for validation
                    all_cells_empty = True
                    for i in range(self.length):
                        cell = board.board[row][col + i]
                        # If at any point in the iteration a cell is found to
                        # not be empty, the flag is set to False and the loop
                        # breaks. The player will then be asked to try again
                        if cell != "~":
                            all_cells_empty = False
                            print("The ship overlaps with another "
                                  "ship. Please try again.")
                            time.sleep(2)
                            clear_terminal()
                            board.print_board()
                            break
                        # If the cell is not empty, the coordinate as added
                        # to the empty list of coordinates
                        else:
                            ship_coords.append((row, col + i))
                    # If the flag remains true after completing each loop
                    # The board will update with the newly placed ship
                    if all_cells_empty:
                        for coord in ship_coords:
                            # Will print the ship in the designated colour
                            board.board[coord[0]][coord[1]] = f"[{self.colour}]S"
                        # Makes the ship coordinates the value in the dict
                        self.ship_coords[self.name] = ship_coords
                        clear_terminal()
                        board.print_board()
                        return board
                        break
            elif direction == "v":
                # If the length of the ship + the length of the board exceed
                # The dimensions, the player is asked to try again
                if (self.length + row) > (board.dimensions + 1):
                    print("The ship doesn't fit. Please try again.")
                    time.sleep(2)
                    clear_terminal()
                    board.print_board()
                    continue
                else:
                    # Creates empty list to append the ships coordinates into
                    ship_coords = []
                    all_cells_empty = True
                    for i in range(self.length):
                        cell = board.board[row + i][col]
                        if cell != "~":
                            all_cells_empty = False
                            print("The ship overlaps with another", end=" ")
                            print("ship. Please try again.")
                            time.sleep(2)
                            clear_terminal()
                            board.print_board()
                            break
                        else:
                            ship_coords.append((row + i, col))
                    if all_cells_empty:
                        for coord in ship_coords:
                            board.board[coord[0]][coord[1]] = f"[{self.colour}]S"
                        self.ship_coords[self.name] = ship_coords
                        clear_terminal()
                        board.print_board()
                        return board
                        break