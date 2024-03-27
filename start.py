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

# All ship instances to be used in the game
battleship = Ships("Battleship", 4, "dark_red", 4)
destroyer_one = Ships("Destroyer 1", 3, "green_4", 3)
destroyer_two = Ships("Destroyer 2", 3, "yellow_4", 3)
submarine_one = Ships("Submarine 1", 2, "dodger_blue1", 2)
submarine_two = Ships("Submarine 2", 2, "blue_violet", 2)

# Player and computer have same ships but having separate
# Lists allows them to be accessed separately when needed
# Specifically in computer_shot() and player_shot()
# So that the correct player's ships decrease in health
player_ships = [
    battleship, destroyer_one, destroyer_two,
    submarine_one, submarine_two
]
computer_ships = [
    battleship, destroyer_one, destroyer_two,
    submarine_one, submarine_two
]

player_board = []
all_ship_coords = []
all_comp_ship_coords = []

user_score = 0
computer_score = 0

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
        # Allows the username to be accessible outside the function
        global user_name
        user_name = input("Enter your name:\n")

        if validate_user_name(user_name):
            print()
            print(f"Welcome aboard [gold3]{user_name}[/gold3]!")
            print("Are you ready to take the seas and win", end = " ")
            print("the [dodger_blue3]Sea Conquest[/dodger_blue3]?\n")
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
    elif len(name) > 28:
        print("This name is too long. Please enter a shorter name.\n")
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

def game_setup():
    # Gets Board class and stores it in a variable to call its methods
    game_board = Board(8)
    # Creates the board and then prints it to the terminal
    game_board.create_board()
    game_board.print_board()

    # global player_ships
    # # Place each ship instance into a list for looping
    # global computer_ships
    global ships

    # List to store all ship coords after placing all ships onto board
    global all_ship_coords
    

    # global player_board
    # player_board = []
    global player_board
    # Iterates over each ship in the list and performs the while loop
    # Once each iteration has been successfully and all ships
    # Have been placed on the board, the for loop stores a copy
    # Of this board into player_board ready to be used for the game
    # Code to use enumerate function adapted from:
    # https://realpython.com/python-enumerate/
    for index, ship in enumerate(player_ships):
        ship.print_ship_information()
        player_board = ship.player_place_ships(game_board)
        all_ship_coords.extend(ship.ship_coords)
        # if index == len(player_ships) - 1:
        #     player_board.append(ships_board.board)

    # An empty list to store a ship's coordinates
    # global computer_ship_coords
    # computer_ship_coords = []
    # All the ships coordinates' are then stored in this list
    # To be accessed during the game
    global all_comp_ship_coords

    print(f"Let the sea conquest begin, commander [gold3]{user_name}[/gold3]!")
    # Calls all the functions from the computer module necessary
    # To create the computer generated board
    computer.create_hidden_comp_board(all_comp_ship_coords, computer_ships)

    time.sleep(2.5)
    clear_terminal()
    start_game()


def start_game():
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

    # breakpoint()
    while True:
        # clear_terminal()
        game.print_blank_and_user_boards(blank_board, user_board, user_name)
        breakpoint()
        col_guess, row_guess = game.player_shot(blank_board, user_name, all_comp_ship_coords, computer_ships)
        time.sleep(1)

        if user_score == 5:
            print("We win!")
            return False

        clear_terminal()
        game.print_blank_and_user_boards(blank_board, user_board, user_name)
        computer.computer_shot(player_board, all_ship_coords, player_ships)
        time.sleep(1)

        if computer_score == 5:
            print("The computer won :(")
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
        print("Type 'I' for instructions or 'S' to start the game.")
        print("Type 'Q' to quit the game.")
        try:
            start_choice = input("Enter 'I', 'S' or 'Q':\n").lower()
            if (start_choice != 'i' and start_choice != 's'
             and start_choice != 'q'):
                raise Exception
            elif start_choice == 'i':
                clear_terminal()
                display_instructions()
            elif start_choice == "s":
                time.sleep(1)
                clear_terminal()
                game_setup()
                return False
            elif start_choice == "q":
                print()
                print("Goodbye for now commander, us", end = " ")
                print("[gold3]Ocean Voyagers[/gold3] are waiting for you!")
                time.sleep(3)
                clear_terminal()
                main()
                return False
        except Exception:
            print('That is not a valid input. Please try again.')


def main():
    """
    Contains all function calls into main function
    """
    print_banner()
    get_user_name()
    game_start_prompt()
