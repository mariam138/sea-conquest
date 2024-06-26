# Imports the Board class to use its methods
from board import Board
# Imports rich module to allow printing in colour
from rich import print
# Imports time module to allow delays before executing code
import time
# Imports the computer module to use its methods
import computer

# Sets the user score to 0 initially
user_score = 0
# Creates an empty list to store the previous guesses in
used_guesses = []


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
    global user_score

    # Sets the width between the boards as a set number
    # This is used to calculate the space that should be printed between
    # Each board and the usernames
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
                print(f"[deep_sky_blue1]{cell}[/deep_sky_blue1]", end=" ")
            print(" " * 30, end=" ")
            for cell in user_row:
                print(f"[deep_sky_blue1]{cell}[/deep_sky_blue1]", end=" ")
            print(" " * 4, end=" ")
            print()
        # Prints "Ships sunk:" between the boards
        elif row == 1:
            print(" " * 4, end=" ")
            for cell in current_row:
                print(cell, end=" ")
            print(" " * 9, end=" ")
            print("Ships sunk:", end=" ")
            print(" " * 8, end=" ")
            for cell in user_row:
                print(cell, end=" ")
            print(" " * 4, end=" ")
            print()
        # Prints "Computer: 0/5" between the boards
        elif row == 2:
            print(" " * 4, end=" ")
            for cell in current_row:
                print(cell, end=" ")
            print(" " * 8, end=" ")
            print(f"[bright_red]Computer[/bright_red]:"
                  f" {computer.computer_score}/5", end=" ")
            print(" " * 7, end=" ")
            for cell in user_row:
                print(cell, end=" ")
            print(" " * 4, end=" ")
            print()
        # Prints the username and the score between boards
        # and centres it depending on the length of the username entered
        elif row == 3:
            print(" " * 4, end=" ")
            for cell in current_row:
                print(cell, end=" ")
            print(" " * ((total_width // 2) - 1), end=" ")
            # Takes away 1 space if the length of the username is even
            if total_width % 2 == 0:
                print(f"[gold3]{username}[/gold3]:"
                      f" {user_score}/5", end=" " * ((total_width // 2)-1))
            # Prints the username as is if the length is odd
            else:
                print(f"[gold3]{username}[/gold3]:"
                      f" {user_score}/5", end=" " * (total_width // 2))
            for cell in user_row:
                print(cell, end=" ")
            print(" " * 4, end=" ")
            print()
        # Prints the rest of both boards as normal
        else:
            print(" " * 4, end=" ")
            for cell in current_row:
                print(cell, end=" ")
            print(" " * 30, end=" ")
            for cell in user_row:
                print(cell, end=" ")
            print(" " * 4, end=" ")
            print()
    print()


def player_shot(board, username, computer_coords, ships):
    """
    Player will enter a valid letter and number coordinate
    to make a guess on where the computer's ships are
    placed. If it's a miss, the computer's board will show
    an "M". If it is a hit, the board will show an "X".
    All guesses will be stored into a list to prevent repeat
    guesses from being made.
    """
    global computer_score
    global user_score
    # Makes the variable global so that it's updated each turn
    global used_guesses

    while True:
        col_guess = board.convert_coord_to_index()
        row_guess = board.validate_number_coord()
        user_guess = (row_guess, col_guess)
        # If the user enters a previously made guess, they will be prompted
        # to enter a new guess
        if user_guess in used_guesses:
            print("You've already guessed that, commander!", end=" ")
            print("Let's try again, shall we?\n")
            continue
        # Checks if the user's guess is in one of the computer's ship coords
        elif user_guess in computer_coords:
            print("Nice shot, Commander!")
            # Adds the guess to the used_guesses list to prevent repeats
            used_guesses.append(user_guess)
            # Iterates through each ship in the player_ships list
            for ship in ships:
                # if the guess is part of one of the ships coordinates
                # the health will decrease by 1.
                if user_guess in ship.ship_coords:
                    print(f"You got their [{ship.colour}]"
                          f"{ship.name}[/{ship.colour}]!\n")
                    # Updates the board with an X in the ship's colour
                    board[row_guess][col_guess] = f"[{ship.colour}]X"
                    ship.health -= 1
                    # Updates the user's score if they sink a ship
                    if ship.health == 0:
                        user_score += 1
                        time.sleep(1.5)
                        print(f"Excellent work, Commander! We sunk the"
                              f" [bright_red]Sea Guardian's[/bright_red]"
                              f" [{ship.colour}]{ship.name}[/{ship.colour}]!")
                    break
            return row_guess, col_guess
        # Updates board with an M and adds the guess to used_guesses
        # If the player guess is a miss
        elif user_guess not in computer_coords:
            print("Argh, we missed... We'll"
                  " get them in the next shot, Commander.")
            used_guesses.append(user_guess)
            board[row_guess][col_guess] = "[grey46]M"
            return row_guess, col_guess
