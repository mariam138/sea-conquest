# To allow printing of certain words in colour to the terminal
from rich import print
# To allow delays before executing certain code
import time


class Board:
    """
    Takes in a number for the dimensions and will print a board out which
    matches these dimensions.
    """

    def __init__(self, dimensions):
        self.dimensions = dimensions
        # Creates an empty list to print out the board and append to
        self.board = []

    # This list of coordinates will be appended to the board and printed out
    horizontal_coords = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]

    def __getitem__(self, index):
        """
        A dunder method to be able to access class objects with
        indices, as if it were an iterable object. This is used later
        in the game when the blank computer board and player board
        are printed side by side. Then the board methods are called to
        enter a row and number to check if the shot is a hit or miss.
        Code to add this dunder method is adapted from:
        https://www.kdnuggets.com/2023/03/\
        introduction-getitem-magic-method-python.html
        """
        return self.board[index]

    def __setitem__(self, index, value):
        """
        A dunder method that can be used side by side with the
        __getitem__ dunder method above. This method will be used when
        the computer takes its shot during gameplay to properly
        update the player_board with either an "M" for miss or
        an "X" for a hit.
        Code to add this dunder method is adapted from:
        https://www.tutorialspoint.com/getitem-and-setitem-in-python
        """
        self.board[index] = value

    def create_board(self):
        """
        Prints the horizontal_coords as a string for the horizontal heading
        row, then loops through a range starting at 1 and ending at
        self.dimensions + 1 to print the numbers for the vertical coordinates.
        Each number is then followed  by the ~ symbol multiplied by the
        dimensions number that has been entered. Using the nested for loop
        creates the game board to be used.
        """

        # Appends list of horizontal coordinates as the top row of the board
        self.board.append(self.horizontal_coords)

        # Loops through the board dimensions starting at 1
        # So that it doesnt start with the letter coordinates row
        for i in range(1, self.dimensions + 1):
            # Creates a list where the first item is a string of the
            # 'i' variable
            row = [str(i)]
            # Loops through and adds a ~ to each row
            # The loop continues based on the dimensions given
            for _ in range(self.dimensions):
                row.append("~")
            # Each row is then appended to the board
            self.board.append(row)
        return self.board

    def print_board(self):
        """
        Prints out the game board that was created, using a nested for loop
        to print a grid to the terminal
        """

        # The enumerate function is used to give an index for each row
        for i, row in enumerate(self.board):
            # Prints the letter coordinates in blue
            if i == 0:
                for cell in row:
                    print(f"[deep_sky_blue1]{cell}[/deep_sky_blue1]", end=" ")
                print()
            else:
                for cell in row:
                    print(cell, end=" ")
                print()
        print()

    def convert_coord_to_index(self):
        """
        When the user is prompted to input a letter coordinate for the game,
        this method converts it into its corresponding index as set up by the
        nested list used to create the board.
        It then validates that the letter the user inputs is in
        the dictionary. If not, the user is asked to try again.
        """

        # A dictionary which contains the letter coordinate as its
        # corresponding number index
        letter_coord_dict = {
            "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8
        }

        #  Checks if vertical_coord is a key in the letter_coord_dict and if
        # so, "converts" it into its value
        # Also allows the user to quit the game at any desired point
        # Whenever prompted to enter a letter coordinate.
        while True:
            print("To quit the game, enter 'Q'.")
            column_coord = (
                input("Please enter a column coordinate"
                      " as a letter:\n").upper()
            )
            if column_coord in letter_coord_dict:
                col = letter_coord_dict[column_coord]
                return col
                # Breaks the while loop once the input is valid
                break
            elif column_coord == "Q":
                # Creates separate while loop for if the user chooses to leave
                while True:
                    print("Are you leaving us Commander?")
                    stay_leave = input(
                        "Type 'Y' to quit, or 'N' to stay:\n").upper()
                    # Exits the program if the user enters "Y"
                    if stay_leave == 'Y':
                        print("You've let us down Commander...")
                        time.sleep(2)
                        print("To restart the game, press the "
                              "'Run Program' button at the top of the page.")
                        exit()
                    # Goes back to the game if the user enters "N"
                    # By breaking the inner while loop
                    elif stay_leave == 'N':
                        print("We knew you weren't a quitter! "
                              "Now, where were we...\n")
                        time.sleep(2)
                        break
                    # Continues loop if user enters anything other than "Y"
                    # or "N"
                    elif (stay_leave != 'Y') and (stay_leave != 'N'):
                        print("I didn't quite catch that Commander! "
                              "Let's try that again.")
                        continue
            else:
                print("That is not a valid coordinate. Please try again.")

    def validate_number_coord(self):
        """
        This method will ask the user to input a row coordinate.
        It will validate whether the number input is within
        the board dimensions. If not, the user is asked to try again.
        """
        while True:
            # Converts the input into an integer for comparisons in
            # the if/elif statement
            try:
                row_coord = (
                    int(input("Please enter a row coordinate as a number:\n"))
                )
                # Breaks loop if the number is within the board dimensions
                if (1 <= row_coord <= self.dimensions):
                    row = row_coord
                    return row
                    return False
                # Loop repeats if a num outside the board dimensions is entered
                elif (row_coord < 1) or (row_coord > self.dimensions):
                    print("That is not a valid coordinate. Please try again.")
                # Raises a value error if any non-numeric input occurs
                elif row_coord.isnumeric() is False:
                    raise ValueError
            except ValueError:
                print("That is not a valid input. Please enter a number.")
