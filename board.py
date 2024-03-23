class Board:
    """
    Takes in a number for the dimensions and will print a board out which
    matches these dimensions.
    """

    def __init__(self, dimensions):
        self.dimensions = dimensions
        # Creates an empty list to print out the board and append to
        self.board = []

    horizontal_coords = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]

    def create_board(self):
        """
        Prints the horizontal_coords as a string for the horizontal heading
        row, then loops through a range starting at 1 and ending at
        self.dimensions + 1 to print the numbers for the vertical coordinates.
        Each number is then followed  by the ~ symbol times the dimensions
        number that has been entered. Using the nested for loop creates the
        game board to be used.
        """
        self.board.append(self.horizontal_coords)

        for i in range(1, self.dimensions + 1):
            row = [str(i)]
            for _ in range(self.dimensions):
                row.append("~")
            self.board.append(row)
        return self.board

    def print_board(self):
        """
        Prints out the game board that was created, using a nested for loop
        to print a grid to the terminal
        """
        for row in self.board:
            for cell in row:
                print(cell,   end=" ")
            print()
        print()

    def convert_coord_to_index(self):
        """
        When the user is prompted to input a letter coordinate for the game,
        this method converts it into its corresponding index as set up by the
        nested list used to create the board.
        It then validates that the inputted letter coordinate is in
        the dictionary. If not, the user is asked to try again.
        """

        # A dictionary which contains the letter coordinate as its
        # corresponding number index
        letter_coord_dict = {
            "A": 1, "B": 2, "C": 3, "D" : 4, "E": 5, "F": 6, "G": 7, "H": 8
        }

        #  Checks if vertical_coord is a key in the letter_coord_dict and if
        # so, "converts" it into its value
        while True:
            column_coord = (
                input("Please enter a column coordinate as a letter:\n").upper()
            )
            if column_coord in letter_coord_dict:
                col = letter_coord_dict[column_coord]
                return col
                break
            else:
                print("That is not a valid coordinate. Please try again.")

    def validate_number_coord(self):
        """
        This method will ask the user to input a row coordinate.
        It will validate whether the number inputted is within
        the board dimensions. If not, the user is asked to try again.
        """
        while True:
            # Converts the input into an integer for comparisons in
            # the if/elif statement
            try:
                row_coord = (
                    int(input("Please enter a row coordinate as an number:\n"))
                )
                if (1 <= row_coord <= self.dimensions):
                    row = row_coord
                    return row
                    return False
                elif (row_coord < 1) or (row_coord > self.dimensions):
                    print("That is not a valid coordinate. Please try again.")
                elif row_coord.isnumeric() is False:
                    raise ValueError
            except ValueError:
                print("That is not a valid input. Please enter a number.")
