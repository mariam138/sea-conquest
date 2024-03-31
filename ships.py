# Imports Board class from board.py module
from board import Board
from clear import clear_terminal
from rich import print


class Ships:
    """
    Predefines the number of ships the player and computer gets.
    Each ship has a predefined length:
    1 x Battleship (length = 4)
    2 x Destroyer (length = 3)
    2 x Submarine (length = 2)
    """
    def __init__(self, name, length, colour, health):
        self.name = name
        self.length = length
        self.colour = colour
        self.health = length
        # Empty list which the ship's coordinates will be stored
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

        ship_names = ship_length.keys()
        ship_lengths = ship_length.values()
        print("You will have 1 Battleship, 2 Destroyers and 2 Submarines.\n")
        for name, length in zip(ship_names, ship_lengths):
            print(f"The {name} has a length of {length}.")
        print("\n")

    def player_place_ships(self, board):
        """ Code that will be used to ask the player to choose
        starting coordinates for their ship to be placed.
        Player will be asked if they want their ship horizontally
        or vertically. Validation will be done before a ship
        is placed to ensure it fits on the board and doesn't
        overlap with other ships placed.
        """
        print("You will now place your ships.")
        while True:
            print(f"Placing [dodger_blue3]{self.name}....\n")
            print("Please enter your starting co-ordinate")
            col = board.convert_coord_to_index()
            row = board.validate_number_coord()
            print("Which direction do you want your ship to be placed?")
            print("Type 'h' for horizontal or 'v' for vertical.")
            direction = input("Please enter 'h' or 'v':\n")
            if direction != "h" and direction != "v":
                print("Invalid direction. Please try again.")
            elif direction == "h":
                if (self.length + col) > (board.dimensions + 1):
                    print("The ship doesn't fit. Please try again.")
                    continue
                else:
                    # Creates empty list to append the ships coordinates into
                    ship_coords = []
                    for i in range(self.length):
                        if board.board[row][col + i] != "~":
                            print("The ship overlaps with another", end=" ")
                            print("ship. Please try again.")
                            break
                        else:
                            for i in range(self.length):
                                board.board[row][col + i] = f"[{self.colour}]S"
                                ship_coords.append((row, col + i))
                            self.ship_coords[self.name] = ship_coords
                        clear_terminal()
                        board.print_board()
                        return board
            elif direction == "v":
                if (self.length + row) > (board.dimensions + 1):
                    print("The ship doesn't fit. Please try again.")
                    continue
                else:
                    ship_coords = []
                    for i in range(self.length):
                        if board.board[row + i][col] != "~":
                            print("The ship overlaps with another", end=" ")
                            print("ship. Please try again.")
                            break
                        else:
                            for i in range(self.length):
                                board.board[row + i][col] = f"[{self.colour}]S"
                                ship_coords.append((row + i, col))
                            self.ship_coords[self.name] = ship_coords
                        clear_terminal()
                        board.print_board()
                        return board
