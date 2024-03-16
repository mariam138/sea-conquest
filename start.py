# Allows the content in the terminal to be printed in colour
from rich import print
# Clears the terminal when the function is called
from clear import clear_terminal
# Allows delay in code execution when called
import time
# Imports Board class to allow printing of board to terminal
from board import Board
# To get information from Ships class to start game
from ships import Ships


def print_banner():
    """
     Prints out the game's banner whenever the game is started
    """
    print()
    print((35 * " ") + "Welcome to" + (35 * " "))
    # Website used to create logo art: https://www.ascii-art-generator.org/
    print(r"""[dodger_blue3]

    ___|               ___|                                   |   
  \___ \   _ \  _` |  |      _ \  __ \   _` | |   |  _ \  __| __| 
        |  __/ (   |  |     (   | |   | (   | |   |  __/\__ \ |   
  _____/ \___|\__,_| \____|\___/ _|  _|\__, |\__,_|\___|____/\__| 
                                          _|                     

  """)


def get_user_name():
    """
      Get the user to input their name into the terminal. A while loop
      is used to determine whether the input is valid or not, by calling
      the validate_user_name method. If valid, the username will then be
      used in the welcome message, and later on will be used
      to keep score of the number of enemy ships destroyed.
      """
    while True:
        print("Type your name below.")
        print("Please use only letters.\n")
        user_name = input("Enter your name:\n")

        if validate_user_name(user_name):
            print()
            print(f"Welcome aboard {user_name}!")
            print("Are you ready to take the seas and win the Sea Conquest?\n")
            break


def validate_user_name(name):
    """
    Validates whether the name entered into the input
    is only alphabetical characters. If characters are
    numerical or special characters, an error message is shown.
    The user is then continuously prompted to enter a new name
    until a valid one is entered.
    """
    if name.isalpha() is False:
        print("That is not a valid input. Please try again.\n")
    else:
        return name


def display_instructions():
    """
    If the user decides to read the instructions before playing, the following
    text is shown, explaining the rules of the game and giving the user
    a background story.Once the instructions are displayed, the user
    will be given the choice to continue
    to game play, or exit back to the starting page.
    """
    print("[purple4]Ocean Voyagers vs Sea Guardians")
    print("Tensions between the rival [bright_red]Sea Guardians[/bright_red]")
    print(" and the [gold3]Ocean Voyagers[/gold3](that's us!) have reached")
    print(" a boiling point. We have to take back what is our rightful sea!")
    print(" As the commander of our naval forces, the ")
    print("[gold3]Ocean Voyagers[/gold3] are putting their trust in you ")
    print("to defeat the [bright_red]Sea Guardian's[/bright_red] ships.")
    print("Get ready to lead the [gold3]Ocean Voyagers[/gold3] to victory!\n")
    print("[purple4]Instructions")
    print("Both you and the enemy will have a grid where your ships shall be")
    print("placed. The objective of the game is to sink all of the")
    print(" [bright_red]Sea Guardian's[/bright_red] ships before they sink")
    print(" ours. We are not able to see the enemy ships, nor will they see ")
    print("ours. Starting with you, you will take the first turn in trying to")
    print(" sink the enemy's ships. The ")
    print("[bright_red]Sea Guardians[/bright_red] will shout 'Hit!' if we")
    print(" hit one of their fleet, or 'Miss' if not. Once all the points of ")
    print("a ship have been hit, it will sink.")
    print("To win the game, we must sink the enemy's ships first.")
    print("Are you ready for the challenge, commander?\n")


def start_game():
    """
    If the user inputs "s" into the terminal, it will trigger this function to
    be called which will start the game. The board will be created, and the
    ships for both the computer and the user will be generated on the board.
    """
    print("Game is starting...")
    # Get user to position ships onto board
    # Create board
    # Create ships
    # Store ships and board somewhere
    # For each ship, get location that user wants
    # For each location, validate: input, if location is valid (does ship fit on board), does ship fit (doesn't overlap with other ships)
    # If validation passes, add ship to board
    # Repeat for other ships
    # Once finished, start game
    # Create two more boards - hidden board for computers ships, blank board for user
    # Add computers ships to board
    # For user, display blank board and their board side by side

    game_board = Board(8)
    game_board.create_board()
    game_board.print_board()


def game_start_prompt():
    """
    This will give the user the choice of either starting the game straight
    away, or asking to read the instructions first. The user is asked to input
    either 's' for starting the game, or 'i' to get the instructions. If any
    other input is given, the terminal will tell the user that the input is
    invalid. Using the while loop, this will keep prompting the user for an
    input until a valid one is given.
    """

    while True:
        print("Would you like to read the instructions or start playing?")
        print("Type 'I' for instructions or 'S' to start the game.")
        print("Type 'Q' to quit the game.")
        try:
            start_choice = input("Enter 'I', 'S' or 'Q':\n").lower()
            if start_choice != 'i' and start_choice != 's' and start_choice != 'q':
                raise Exception
            elif start_choice == 'i':
                clear_terminal()
                display_instructions()
            elif start_choice == "s":
                clear_terminal()
                start_game()
                break
            elif start_choice == "q":
                print()
                print("Goodbye for now commander, us ")
                print("[gold3]Ocean Voyagers[/gold3] are waiting for you!")
                time.sleep(5)
                clear_terminal()
                main()
                break
        except Exception:
            print('That is not a valid input. Please try again.')


def main():
    """
    Contains all function calls into main function
    """
    print_banner()
    get_user_name()
    game_start_prompt()
