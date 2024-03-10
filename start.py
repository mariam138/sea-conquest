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
      print("Are you ready to take the seas and win the Sea Conquest?")
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

get_user_name()
