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

    print()
    print(f"{' ' * 10}"
    f"[bright_red]Computer[/bright_red]"
    f"{' ' * 41}"
    f"[gold3]{username}")
    print()
    for i in range(len(blank_board)):
        # print("Computer")
        print(" " * 4, end = " ")
        for cell in blank_board[i]:
            print(cell, end = " ")
        print(" " * 30, end = " ")
        # print(username)
        for cell in player_board[i]:
            print(cell, end = " ")
        print(" " * 4, end = " ")
        print()
    print()


