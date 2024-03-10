# Allows the content in the terminal to be printed in colour 
from rich import print

print()
print((35 * " ") + "Welcome to" + (35 * " "))
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
  Get the user to input their name into the terminal. 
  The username will then be used in the welcome message, and
  later on in the game will be used to keep score
  of the number of enemy ships destroyed.
  """
  # try:
  user_name = input("Enter your name: ")
  # except:
  #   if user_name.isalpha() == False:
  #     print("That is not a valid input. Please try again.")
  validate_user_name(user_name)

  print()
  print(f"Welcome aboard {user_name}!")
  print("Are you ready to take the seas and win the Sea Conquest?")

def validate_user_name(name):
  """
  Validates whether the name entered into the input
  is only alphabetical characters. If characters are
  numerical or special characters, an error message is shown.
  """
  if name.isalpha() == False:
      print("That is not a valid input. Please try again.")


get_user_name()
