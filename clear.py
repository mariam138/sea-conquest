# Import os module for use in the clear_terminal function
import os

def clear_terminal():
    """
    Function to clear the terminal when called
    Code adapted from:
    https://www.codingninjas.com/studio/library/how-to-clear-a-screen-in-python
    """
    os.system("cls" if os.name == "nt" else "clear")