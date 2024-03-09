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
  user_name = input("Enter your name: ")

  print()
  print(f"Welcome aboard {user_name}!")
  print("Are you ready to take the seas and win the Sea Conquest?")

get_user_name()
