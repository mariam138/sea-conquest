# Imports the Board class to create and print a new blank board
from board import Board
# Imports the necessary variables to be used to display the game
from start import player_board, game_setup

def print_blank_and_user_boards():
    """
    Will print a blank board to represent the computer's ships,
    and print the user's board which was just created side by side.
    Will also print how many of each player's ships have sunk,
    and this will be updated throughout the game.
    """

    blank_board = Board(8)
    blank_board = blank_board.create_board()

    # blank_board.print_board()

    player_board = [
        [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        ['1', 'S', 'S', 'S', 'S', '~', '~', '~', '~'],
        ['2', 'S', 'S', 'S', '~', '~', '~', '~', '~'],
        ['3', 'S', 'S', 'S', '~', '~', '~', '~', '~'],
        ['4', 'S', 'S', '~', '~', '~', '~', '~', '~'],
        ['5', 'S', 'S', '~', '~', '~', '~', '~', '~'],
        ['6', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['7', '~', '~', '~', '~', '~', '~', '~', '~'],
        ['8', '~', '~', '~', '~', '~', '~', '~', '~']
    ]

    print()
    for i in range(len(blank_board)):
        print(" " * 4, end = " ")
        for cell in blank_board[i]:
            print(cell, end = " ")
        print(" " * 40, end = " ")
        for cell in player_board[i]:
            print(cell, end = " ")
        print(" " * 4, end = " ")
        print()
    print()
    # player_board.print_board()
    # print(blank_board)
    # print(player_board)

print_blank_and_user_boards()