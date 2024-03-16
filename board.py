class Board:
    """
    Takes in a number for the dimensions and will print a board out which matches these dimensions.
    """
    
    def __init__(self, dimensions):
        self.dimensions = dimensions
        # Creates an empty list to print out the board and append to
        self.board = []

    horizontal_coords = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]

    def create_board(self):
        """
        Prints the horizontal_coords as a string for the horizontal heading row, then loops through a range starting at 1 and ending at self.dimensions + 1 to print the numbers for the vertical coordinates. Each number is then followed by the ~ symbol times the dimensions number that has been entered. Using the nested for loop creates the game board to be used.
        """
        self.board.append(self.horizontal_coords)

        for i in range(1, self.dimensions + 1):
            row = [str(i)]
            for _ in range(self.dimensions):
                row.append("~")
            self.board.append(row)

    def print_board(self):
        for row in self.board:
            for cell in row:
                print(cell, end = " ")
            print()
    
    def convert_coord_to_index(self):
        letter_coord_dict = {"a": 1, "b": 2, "c": 3, "d" : 4, "e": 5, "f": 6, "g": 7, "h": 8}

        vertical_coord = (input("Enter vertical coordinate:\n")).lower()

        if vertical_coord in letter_coord_dict:
            coord = letter_coord_dict[vertical_coord]
            print(coord)

game_board = Board(8)
game_board.create_board()
game_board.print_board()
game_board.convert_coord_to_index()