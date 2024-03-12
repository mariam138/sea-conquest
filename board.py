
# print(horizontal_coords)
# print(" ", "A", "B", "C", "D", "E", "F", "G", "H")
# print("1", (("~" + " ") * 8))

class Board:
    """
    Takes in a number for the dimensions and will print a board out which matches these dimensions.
    """
    
    def __init__(self, dimensions):
        self.dimensions = dimensions

    horizontal_coords = ["A", "B", "C", "D", "E", "F", "G", "H"]

    def create_board(self):
        print(self.horizontal_coords)
        

game_board = Board(8)
game_board.create_board()
# ''.join([str(elem) for elem in my_list])