# Allows the content in the terminal to be printed in colour 
from rich import print
# Clears the terminal when the function is called
from clear import clear_terminal

print()
print((35 * " ") + "Welcome to" + (35 * " "))
# Website used to create logo art: https://www.ascii-art-generator.org/
print("""[dodger_blue3]

  _|_|_|                            _|_|_|                                                                _|      
_|          _|_|      _|_|_|      _|          _|_|    _|_|_|      _|_|_|  _|    _|    _|_|      _|_|_|  _|_|_|_|  
  _|_|    _|_|_|_|  _|    _|      _|        _|    _|  _|    _|  _|    _|  _|    _|  _|_|_|_|  _|_|        _|      
      _|  _|        _|    _|      _|        _|    _|  _|    _|  _|    _|  _|    _|  _|            _|_|    _|      
_|_|_|      _|_|_|    _|_|_|        _|_|_|    _|_|    _|    _|    _|_|_|    _|_|_|    _|_|_|  _|_|_|        _|_|  
                                                                      _|                                          
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
    user_name = input("Enter your name: ")

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
  if name.isalpha() == False:
    print("That is not a valid input. Please try again.\n")
  else:
    return name

def display_instructions():
  """
  If the user decides to read the instructions before playing, the following
  text is shown, explaining the rules of the game and giving the user a background story.
  Once the instructions are displayed, the user will be given the choice to continue
  to game play, or exit back to the starting page.
  """
  print("[purple4]Ocean Voyagers vs Sea Guardians")
  print("Tensions between the rival [bright_red]Sea Guardians[/bright_red] and the [gold3]Ocean Voyagers[/gold3] (that's us!) have reached a boiling point. We have to take back what is our rightful sea! As the commander of our naval forces, the [gold3]Ocean Voyagers[/gold3] are putting their trust in you to defeat the [bright_red]Sea Guardian's[/bright_red] ships.")
  print("Get ready to lead the [gold3]Ocean Voyagers[/gold3] to victory!")
  print()
  print("[purple4]Instructions")
  print("Both you and the enemy will have a grid where your ships shall be placed. The objective of the game is to sink all of the [bright_red]Sea Guardian's[/bright_red] ships before they sink ours. We are not able to see the enemy ships, nor will they see ours.")
  print("Starting with you, you will take the first turn in trying to sink the enemy's ships. The [bright_red]Sea Guardians[/bright_red] will shout 'Hit!' if we hit one of their fleet, or 'Miss' if not. Once all the points of a ship have been hit, it will sink.")
  print("To win the game, we must sink the enemy's ships first. Are you ready for the challenge, commander?")

def game_start_prompt():
  """
  This will give the user the choice of either starting the game straight
  away, or asking to read the instructions first. The user is asked to input either 's' for starting the game, or 'i' to get the instructions. If any other input is given, the terminal will tell the user that the input is invalid. Using the while loop, this will keep prompting the user for an input until a valid one is given.
  """
  print("Would you like to read the instructions or start playing?")
  print("Type 'I' for instructions or 'S' to start the game.")

  while True:
    try:
      start_choice = input("Enter 'I' or 'S': ").lower()
      if start_choice != 'i' and start_choice != 's':
          raise Exception
      elif start_choice == 'i':
        clear_terminal()
        display_instructions()
        break
      elif start_choice == "s":
        clear_terminal()
        print("Hello")
        break
    except Exception:
      print('That is not a valid input. Please try again.')



get_user_name()
game_start_prompt()
