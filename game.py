# Imports the Board class to use its methods
from board import Board
from rich import print

def print_blank_and_user_boards(blank_board, player_board, username):
    """
    Will print a blank board to represent the computer's ships,
    and print the user's board which was just created side by side.
    Will also print how many of each player's ships have sunk,
    and this will be updated throughout the game.
    """
    # Makes the scores global so that they can be accessed in a
    # Different function later on in the module
    global computer_score
    computer_score = 0
    global user_score
    user_score = 0

    width_between_boards = 30
    total_width = (
        width_between_boards - (len(username) + len(str(user_score) + "/5"))
    )

    print()
    # Labels each board so user knows which board is which
    print(f"{' ' * 10}"
    f"[bright_red]Computer[/bright_red]"
    f"{' ' * 41}"
    f"[gold3]{username}[/gold3]")
    print()
    # A nested for loop to print one row of the blank board
    # Followed by one row of the user board side by side
    for row in range(blank_board.dimensions + 1):
        current_row = blank_board[row]
        user_row = player_board[row]
        # Will print the letter coordinates row in colour
        if row == 0:
            print(" " * 4, end=" ")
            for cell in current_row:
                print(f"[deep_sky_blue1]{cell}[/deep_sky_blue1]", end = " ")
            print(" " * 30, end = " ")
            for cell in user_row:
                print(f"[deep_sky_blue1]{cell}[/deep_sky_blue1]", end = " ")
            print(" " * 4, end = " ")
            print()
        # Prints "Ships sunk:" between the boards
        elif row == 1:
            print(" " * 4, end = " ")
            for cell in current_row:
                print(cell, end = " ")
            print(" " * 9, end = " ")
            print("Ships sunk:", end = " ")
            print(" " * 8, end = " ")
            for cell in user_row:
                print(cell, end = " ")
            print(" " * 4, end = " ")
            print()
        # Prints "Computer: 0/5" between the boards
        elif row == 2:
            print(" " * 4, end = " ")
            for cell in current_row:
                print(cell, end = " ")
            print(" " * 8, end = " ")
            print(f"[bright_red]Computer[/bright_red]:"
            f" {computer_score}/5", end = " ")
            print(" " * 7, end = " ")
            for cell in user_row:
                print(cell, end = " ")
            print(" " * 4, end = " ")
            print()
        # Prints the username and the score between boards
        # and centres it depending on the length of the username entered
        elif row == 3:
            print(" " * 4, end = " ")
            for cell in current_row:
                print(cell, end = " ")
            print(" " * ((total_width // 2) - 1), end = " ")
            if total_width % 2 == 0:
                print(f"[gold3]{username}[/gold3]:"
                f" {user_score}/5", end = " " * ((total_width // 2)-1))
            else:
                print(f"[gold3]{username}[/gold3]:"
                f" {user_score}/5", end = " " * (total_width // 2))
            for cell in user_row:
                print(cell, end = " ")
            print(" " * 4, end = " ")
            print()
        # Prints the rest of both boards as normal
        else:
            print(" " * 4, end = " ")
            for cell in current_row:
                print(cell, end = " ")
            print(" " * 30, end = " ")
            for cell in user_row:
                print(cell, end = " ")
            print(" " * 4, end = " ")
            print()
    print()

def player_shot(board, username, computer_ship_coords):
    """
    Player will enter a valid letter and number coordinate
    to make a guess on where the computer's ships are
    placed. If it's a miss, the computer's board will show
    an "M". If it is a hit, the board will show an "X". 
    All guesses will be stored into a list to prevent repeat
    guesses from being made.
    """

    print(f"It's our turn first, commander {username}!")
    print("Take your best shot for the", end = " ")
    print("[gold3]Ocean Voyagers[/gold3]!\n")
    row_guess = board.validate_number_coord()
    col_guess = board.convert_coord_to_index()

    user_guess = (row_guess, col_guess)
    if user_guess in computer_ship_coords:
        print("Hit!")
    elif user_guess not in computer_ship_coords:
        print("Miss :(")
