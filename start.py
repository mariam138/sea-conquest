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
# Imports the computer module to access its functions
import computer
# Imports game module to use its methods
import game

# All player ship instances to be used in the game
player_battleship = Ships("Battleship", 4, "bright_magenta", 4)
player_destroyer_one = Ships("Destroyer 1", 3, "green4", 3)
player_destroyer_two = Ships("Destroyer 2", 3, "dark_olive_green1", 3)
player_submarine_one = Ships("Submarine 1", 2, "blue3", 2)
player_submarine_two = Ships("Submarine 2", 2, "purple4", 2)

# All computer ship instances to be used in the game
comp_battleship = Ships("Battleship", 4, "bright_magenta", 4)
comp_destroyer_one = Ships("Destroyer 1", 3, "green4", 3)
comp_destroyer_two = Ships("Destroyer 2", 3, "dark_olive_green1", 3)
comp_submarine_one = Ships("Submarine 1", 2, "blue3", 2)
comp_submarine_two = Ships("Submarine 2", 2, "purple4", 2)

# All player's ship instances and computer's ships instances are placed
# Into separate lists to be used as arguments in functions for the game
player_ships = [
    player_battleship, player_destroyer_one, player_destroyer_two,
    player_submarine_one, player_submarine_two
]
computer_ships = [
    comp_battleship, comp_destroyer_one, comp_destroyer_two,
    comp_submarine_one, comp_submarine_two
]

# Initialises varibales as empty lists to be used in the functions below
player_board = []
all_ship_coords = []
all_comp_ship_coords = []


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
        print("Please use only letters. "
              "The maximum length is 28 characters.\n")
        # Allows the username to be accessible outside the function
        global user_name
        user_name = input("Enter your name:\n")

        if validate_user_name(user_name):
            print()
            print(f"Welcome aboard [gold3]{user_name}[/gold3]!")
            print("Are you ready to take the seas and win", end=" ")
            print("the [dodger_blue3]Sea Conquest[/dodger_blue3]?\n")
            break


def validate_user_name(name):
    """
    Validates whether the name entered into the input
    is only alphabetical characters. If characters are
    numerical or special characters, an error message is shown.
    Also checks for the length of the username. If the length is over
    28, the user will be warned and asked to enter a shorter name.
    The user is then continuously prompted to enter a new name
    until a valid one is entered.
    """
    if name.isalpha() is False:
        print("That is not a valid input. Please try again.\n")
    elif len(name) > 28:
        print("This name is too long. Please enter a shorter name.\n")
    else:
        return name


def display_instructions():
    """
    If the user decides to read the instructions before playing, the following
    text is shown, explaining the rules of the game and giving the user
    a background story. Once the instructions are displayed, the user
    will be given the choice to continue to game play,
    or exit back to the starting page.
    """
    print("[purple4]Ocean Voyagers vs Sea Guardians")
    print("Tensions between the rival [bright_red]Sea Guardians[/bright_red]"
          " and the [gold3]Ocean Voyagers[/gold3](that's us!)")
    print("have reached a boiling point. We have to take back what"
          "is our rightful sea!")
    print("As the commander of our naval forces, the "
          "[gold3]Ocean Voyagers[/gold3] are putting")
    print("their trust in you to defeat the "
          "[bright_red]Sea Guardians[/bright_red].")
    print("Get ready to lead the [gold3]Ocean Voyagers[/gold3] to victory!\n")
    print("[purple4]Instructions")
    print("Both you and the enemy will have a grid where your ships shall be "
          "placed.")
    print("The objective of the game is to sink all of the"
          " [bright_red]Sea Guardian's[/bright_red]")
    print("ships before they sink ours. We are not able to see the"
          "enemy ships,")
    print("nor will they see ours. Starting with you, you will take "
          "the first turn")
    print("in trying to sink the enemy's ships. The "
          "[bright_red]Sea Guardians[/bright_red]")
    print("will shout if we have [red3]hit[/red3] one of their fleet"
          " or if we have [yellow1]missed[/yellow1].")
    print("Once all the coordinates of a ship have been hit, it will"
          "[red3]sink[/red3].")
    print("To win the game, we must sink the enemy's ships first.")
    print("Are you ready for the challenge, commander?\n")


def game_setup():
    # Gets Board class and stores it in a variable to call its methods
    game_board = Board(8)
    # Creates the board and then prints it to the terminal
    game_board.create_board()
    game_board.print_board()

    # Makes the player_ships list accessible within the function
    global player_ships
    # List to store all ship coords after placing all ships onto board
    global all_ship_coords
    # Makes the player_board global to update it for each ship placement
    global player_board

    # Iterates over each ship in the list and performs the while loop
    # Code to use enumerate function adapted from:
    # https://realpython.com/python-enumerate/
    for index, ship in enumerate(player_ships):
        ship.print_ship_information()
        player_board = ship.player_place_ships(game_board)

        # Gets value from each dict and stores it in ship_coords
        ship_coords = ship.ship_coords[ship.name]
        # Adds each of the ship_coords lists to all_ship_coords
        # This variable is then used in computer_shot()
        all_ship_coords.extend(ship.ship_coords.values())

    # Flattens out the above nested list into one list
    # Code adapted from:
    # https://realpython.com/python-flatten-list/
    # using-a-comprehension-to-flatten-a-list-of-lists
    all_ship_coords = [
        coord for sublist in all_ship_coords for coord in sublist
        ]

    # All the ships coordinates' are then stored in this list
    # To be accessed during the game
    global all_comp_ship_coords

    print(f"Let the sea conquest begin, commander [gold3]{user_name}[/gold3]!")
    # Calls all the functions from the computer module necessary
    # To create the computer generated board
    computer.create_hidden_comp_board(all_comp_ship_coords, computer_ships)

    time.sleep(2.5)
    clear_terminal()
    start_game(user_name)


def restart_or_exit_game(username):
    """
    At the end of the game, once either the computer
    or the player have sunk all of the opponents ships,
    this prompt will appear asking the user if they would
    like to play again or exit the game entirely.
    """

    while True:
        print(f"Would you like to start another game Commander"
              f" [gold3]{username}[/gold3]?")
        print("Enter 'S' to start a new game, or enter 'Q' to exit.")
        try:
            # Expects an error to occur during user input
            end_choice = input("Enter 'S' or 'Q':\n").lower()
            if (end_choice != "q" and end_choice != "s"):
                raise Exception
                # Starts game again from game setup
            elif end_choice == "s":
                print()
                print(f"You've got heart, Commander [gold3]{username}[/gold3]!"
                      f" Let's battle the [bright_red]Sea Guardians"
                      "[/bright_red] again!")
                time.sleep(2.5)
                clear_terminal()
                game_setup()
                return False
            # Leaves game and goes back to 'starting page'
            elif end_choice == "q":
                print()
                print(f"You've worked hard, Commander [gold3]{username}.")
                print("Us [gold3]Ocean Voyagers[/gold3] will be", end=" ")
                print("waiting for you!")
                time.sleep(2.5)
                clear_terminal()
                main()
                return False
        # Handles invalid input and makes user enter a valid input
        except Exception:
            print("That was not a valid input. Please try again.\n")


def start_game(username):
    """
    If the user inputs "s" into the terminal, it will trigger this function to
    be called which will start the game. The board will be created, and the
    ships for both the computer and the user will be generated on the board.
    """
    # Creates a blank board instance from the Board class
    blank_board = Board(8)
    blank_board.create_board()

    # Using the global variable player_board, the actual
    # board object itself is stored into another variable
    # To then be used to print both boards side by side
    global user_board
    user_board = player_board.board

    print(f"It's our turn first, Commander [gold3]{username}[/gold3]!")
    print("Take your best shot for the", end=" ")
    print("[gold3]Ocean Voyagers[/gold3]!\n")

    # Sets variable to true so that the print statement below
    # only prints after the first loop
    first_iteration = True

    while True:
        # Will only print this line after the first loop
        if not first_iteration:
            print(f"It's our turn again, Commander [gold3]{username}[/gold3]!")
        else:
            first_iteration = False

        game.print_blank_and_user_boards(blank_board, user_board, user_name)
        col_guess, row_guess = game.player_shot(
            blank_board, user_name, all_comp_ship_coords, computer_ships
            )
        time.sleep(2)

        # Game ends if the user sinks all 5 ships
        # User is then asked if they want to play again or leave
        if game.user_score == 5:
            clear_terminal()
            # Banner generated from:
            # https://patorjk.com/software/taag/#p=display&f=Graffiti&t=
            print(r"""
                              [bright_green]
                 __   _____  _   _  __        _____ _   _ _
                 \ \ / / _ \| | | | \ \      / /_ _| \ | | |
                  \ V / | | | | | |  \ \ /\ / / | ||  \| | |
                   | || |_| | |_| |   \ V  V /  | || |\  |_|
                   |_| \___/ \___/     \_/\_/  |___|_| \_(_)
                    """)

            restart_or_exit_game(user_name)
            return False

        clear_terminal()
        # Game continues to computer's turn if user score isn't 5
        game.print_blank_and_user_boards(blank_board, user_board, user_name)
        print("It's the [bright_red]Sea Guardians'[/bright_red] turn...")
        time.sleep(2)
        computer.computer_shot(player_board, all_ship_coords, player_ships)
        time.sleep(2)
        clear_terminal()

        # Ends game if the computer reaches a score of 5
        # Again asks user if they want to play again or leave
        if computer.computer_score == 5:
            clear_terminal
            print(r"""[red3]
                  __   __            _
                  \ \ / /__  _   _  | | ___  ___  ___
                   \ V / _ \| | | | | |/ _ \/ __|/ _ \
                    | | (_) | |_| | | | (_) \__ \  __/_ _ _
                    |_|\___/ \__,_| |_|\___/|___/\___(_|_|_)
            """)

            restart_or_exit_game(user_name)
            return False


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
        print("Type 'I' for instructions or 'S' to start the game. "
              "Type 'Q' to quit the game.")
        # Expects an error from invalid user input
        try:
            start_choice = input("Enter 'I', 'S' or 'Q':\n").lower()
            if (start_choice != 'i' and start_choice != 's'
               and start_choice != 'q'):
                raise Exception
            # Displays the instructiions
            elif start_choice == 'i':
                clear_terminal()
                display_instructions()
            # Starts the game with the game setup
            elif start_choice == "s":
                time.sleep(1)
                clear_terminal()
                game_setup()
                return False
            # Quits game and returns back to 'starting page'
            elif start_choice == "q":
                print()
                print("Goodbye for now commander, us", end=" ")
                print("[gold3]Ocean Voyagers[/gold3] are waiting for you!")
                time.sleep(3)
                clear_terminal()
                main()
                return False
        # In case of invalid input, user will be asked to try again
        except Exception:
            print("That is not a valid input. Please try again.\n")


def main():
    """
    Contains all function calls into main function
    """
    print_banner()
    get_user_name()
    game_start_prompt()
