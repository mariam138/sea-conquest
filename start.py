print()
print((35 * " ") + "Welcome to" + (35 * " "))
print("""
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
  user_name = input("Enter your name: ")

  print()
  print(f"Welcome aboard {user_name}!")
  print("Are you ready to take the seas and win the Sea Conquest?")

get_user_name()
