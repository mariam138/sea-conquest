# Imports the main() function from the start module to start the game
from start import main

# Python assigns the __name__ variable a value of __main__ if
# it's the initial module being ran
# As this module is the initial module being ran for the game,
# it will call the main() function that has been imported from the
# start module
# Code is adapted from: https://www.youtube.com/watch?v=OBabwRH0XUo
if __name__ == '__main__':
    main()