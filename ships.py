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
    def __init__(self, name, length):
        self.name = name
        self.length = length
        
    

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
    

    def player_place_ships(self, game_board):
        """ Code that will be used to ask the player to choose
        starting coordinates for their ship to be placed.
        Player will be asked if they want their ship horizontally
        or vertically. Validation will be done before a ship
        is placed to ensure it fits on the board and doesn't
        overlap with other ships placed.
        """
       
        

        print("You will now place your ships.")
        while True:
            print("Please enter your starting co-ordinate")
            col = game_board.convert_coord_to_index()
            row = game_board.validate_number_coord()
            print("Which direction do you want your ship to be placed?")
            print("Type 'h' for horizontal or 'v' for vertical.")
            direction = input("Please enter 'h' or 'v':\n")
            if direction != "h" and direction != "v":
                print("That is not a valid input. Please try again.")
            elif direction == "h":
                if (self.length + col) > (game_board.dimensions + 1):
                    print("The ship doesn't fit. Please try again.")
                else:
                    for i in range(self.length):
                        game_board.board[row][col + i] = "S"
                    game_board.print_board()
                    break
                

       
    
  
game_board = Board(8)
game_board.create_board()
game_board.print_board()
battleship = Ships("Battleship", 4)
battleship.player_place_ships(game_board)