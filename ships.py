# Imports Board class from board.py module
from board import Board

class Ships:
    """
    Predefines the number of ships the player and computer gets.
    Each ship has a predefined length:
    1 x Battleship (length = 4)
    2 x Destroyer (length = 3)
    2 x Submarine (length = 2)
    """
    def __init__(self, length):
        self.length = length
    

    def print_ship_information(self):
        # Defines each ship length in a dictionary to be used in other methods
        ship_length = {
            "Battleship": 4,
            "Destroyer": 3,
            "Submarine": 2
        }

        ship_names = ship_length.keys()
        ship_lengths = ship_length.values()
        for name, length in zip(ship_names, ship_lengths):
            print(f"The {name} has a length of {length}")
        print("You will have 1 Battleship, 2 Destroyers and 2 Submarines.")

    def player_place_ships(self):
        
    

    # Converts letter input to uppercase and stores it into vertical_coord variable
    # vertical_coord = (input("Enter vertical coordinate:\n")).upper()
    # Board.convert_coord_to_index(vertical_coord)
    
  
game_board = Board(8)
game_board.print_board()