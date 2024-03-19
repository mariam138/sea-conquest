# This module creates a function to clear the terminal when called
# The code is adapted from https://www.codingninjas.com/studio/library/how-to-clear-a-screen-in-python
import os

def clear_terminal():
    os.system("cls" if os.name === "nt" else "clear")
    
    # if os.name == "nt":
    #     _ = os.system("cls")
    # else:
    #     _ = os.system("clear")
