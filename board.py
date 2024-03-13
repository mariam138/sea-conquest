class Board:
    """
    Takes in a number for the dimensions and will print a board out which matches these dimensions.
    """
    
    def __init__(self, dimensions):
        self.dimensions = dimensions

    horizontal_coords = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]

    def create_board(self):
        """
        Prints the horizontal_coords as a string for the horizontal heading row, then loops through a range starting at 1 and ending at self.dimensions + 1 to print the numbers for the vertical coordinates. Each number is then followed by the ~ symbol times the dimensions number that has been entered. Using the nested for loop creates the game board to be used.
        """
        # Prints list as a string for the horizontal coordinates
        print(" ".join(self.horizontal_coords))
        # 'end = " "' overrides print function's default '\n' at the end
        for i in range(1, self.dimensions + 1):
            print(i, end=" ")
            for _ in range(self.dimensions):
                print("~", end=" ")
            print()
        

game_board = Board(8)
game_board.create_board()