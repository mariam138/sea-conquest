# Imports the Board class to create and print a new blank board
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

    # breakpoint()
    width_between_boards = 30
    total_width = width_between_boards - (len(username) + len(str(user_score) + "/5"))

    print()
    # Labels each board so user knows which board is which
    print(f"{' ' * 10}"
    f"[bright_red]Computer[/bright_red]"
    f"{' ' * 41}"
    f"[gold3]{username}[/gold3]")
    print()
    # A nested for loop to print one row of the blank board
    # Followed by one row of the user board side by side
    for i in range(len(blank_board)):
        # Will print the letter coordinates row in colour
        if i == 0:
            print(" " * 4, end=" ")
            for cell in blank_board[i]:
                print(f"[deep_sky_blue1]{cell}[/deep_sky_blue1]", end = " ")
            print(" " * 30, end = " ")
            for cell in player_board[i]:
                print(f"[deep_sky_blue1]{cell}[/deep_sky_blue1]", end = " ")
            print(" " * 4, end = " ")
            print()
        elif i == 1:
            print(" " * 4, end = " ")
            for cell in blank_board[i]:
                print(cell, end = " ")
            print(" " * 9, end = " ")
            print("Ships sunk:", end = " ")
            print(" " * 8, end = " ")
            for cell in player_board[i]:
                print(cell, end = " ")
            print(" " * 4, end = " ")
            print()
        elif i == 2:
            print(" " * 4, end = " ")
            for cell in blank_board[i]:
                print(cell, end = " ")
            print(" " * 8, end = " ")
            print(f"[bright_red]Computer[/bright_red]:"
            f" {computer_score}/5", end = " ")
            print(" " * 7, end = " ")
            for cell in player_board[i]:
                print(cell, end = " ")
            print(" " * 4, end = " ")
            print()
        elif i == 3:
            print(" " * 4, end = " ")
            for cell in blank_board[i]:
                print(cell, end = " ")
            print(" " * ((total_width // 2) - 1), end = " ")
            if total_width % 2 == 0:
                print(f"[gold3]{username}[/gold3]:"
                f" {user_score}/5", end = " " * ((total_width // 2)-1))
            else:
                print(f"[gold3]{username}[/gold3]:"
                f" {user_score}/5", end = " " * (total_width // 2))
            for cell in player_board[i]:
                print(cell, end = " ")
            print(" " * 4, end = " ")
            print()
        else:
            print(" " * 4, end = " ")
            for cell in blank_board[i]:
                print(cell, end = " ")
            print(" " * 30, end = " ")
            for cell in player_board[i]:
                print(cell, end = " ")
            print(" " * 4, end = " ")
            print()
    print()


