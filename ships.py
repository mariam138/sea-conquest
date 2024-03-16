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
    
