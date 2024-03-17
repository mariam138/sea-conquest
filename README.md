# Sea Conquest
## Introduction

Sea Conquest is a browser-based game created in Python. This game is based on the classic *BattleShips* game. 

## User Stories

## Features

### Logic Flow

Before starting to create the game, I made some logic flow diagrams of how I wanted the basic structure of the game to work. The first flow diagram I made was the basic logic of the start of the game. First I wanted the user to input their name, which would have input validation. The game would not move on until valid input is present. Once a valid name is entered, the user is given the choice of either reading the instructions or jumping straight into the game. If the user chooses to read the instructions, they are then given the choice to either continue to the game or go back to the start page.

![start-game-logic](https://github.com/mariam138/sea-conquest/assets/150139337/7734a44e-c40b-4e87-b623-914f0d97de23)

I then made a separate flow chart for the main logic of the game.

![main-game-logic](https://github.com/mariam138/sea-conquest/assets/150139337/4a02615f-e6d3-44ec-bd82-cadec0e1f3de)

Throughout the game, there will be the option for the user to leave the game and go back to the home page. This will be when user input is required for the user's guess. 

These logic flow diagrams are what I have used to base the code of the game on.

### Start Page

The start of the game prints out a logo with the game's name "Sea Conquest." Immediately afterwords, the game asks the user for their name. Username validation occurs, as the game asks only for letters. If any numbers or special characters are entered, an error message appears telling the user that the input is invalid. The user will then be prompted againt to enter a name. Once a valid name has been given, the game will welcome the user.

### Future Features

## Testing

## Ongoing Testing

Throughout the creation of the game, I would check my code using [Python Tutor](https://pythontutor.com/) to ensure that my code was working as I wanted it to. For example, to create the while loop at the start of the game which validates the user's name on input.

### Manual Testing

### Bugs

1. At the start of the game after entering the name, I wanted to give the user a choice of either immediately starting the game or reading the instructions first. To do this, I set up and if/elif statement:

    ` if start_choice == "I" or "i":
        clear_terminal()
        display_instructions()
    elif start_choice == "S" or "s":
        clear_terminal()
        print("Hello") `
    
    However, when testing in my local terminal, this didn't seem to work as typing any letter would show the instructions regardless. To fix this bug, I instead put the code into a 'try except' block:

    ` try:
    start_choice = input("Enter 'I' or 'S': ").lower()
    if start_choice != 'i' and start_choice != 's':
        raise Exception
    elif start_choice == 'i':
        clear_terminal()
        display_instructions()
    elif start_choice == "s":
        clear_terminal()
        print("Hello")
  except Exception:
    print('That is not a valid input. Please try again.')
    `

    This then fixed the issue of the instructions showing regardless of the letter input.

2. Upon initial deployment after building the start screen of the game, the game would not load in the terminal due to a **ModuleNotFoundError"** saying that the **"rich"** module was not named. I had initially installed the **rich** module using the git terminal, which came up with the message saying the requirement was already satisfied. Although I used the commant `pip3 freeze > requirements.txt` to make sure all my dependencies were in place before deployment, the **rich** module did not seem to add. Therefore, I manually added it into the .txt file. This fixed the issue and the app deployed properly.

3. In my **game_start_prompt()** function, I have set up a while loop which only breaks when a valid choice has been entered for either starting the game, reading the instructions or quitting the game. When I had set this up initially, I tested out the loop with several valid and invalid inputs before allowing the loop to break. I found that occasionally, when I had looped a few times, when entering **"S"** to start the game, the print statement which asks the user to select a choice would still appear underneath when it should not. I fixed this bug by adding a simple **"break"** statement if the user chooses to quit the game, as originally I had not. 

4. When creating the board in the **board.py** module, I had initially set up the function to create the board as a nested list of the coordinates but using print statements. When I ran this through **Python Tutor**, each value when creating the board would show as **"None"** rather than either the number/letter coordinates or the "~" symbol. To fix this, I instead made separate functions for creating the board and then printing out the board. After running this through **Python Tutor** again, each list element showed their value rather than **"None"**.

5. After setting up my two validation functions in the Board class for the coordinates (**convert_coord_to_index** and **validate_number_coord**) and adding these into the game_start() function, a bug occurred with the **validate_number_coord** method. If anything but a number was entered, rather than having an error message saying that it wasn't valid, it would trigger the **game_start_prompt** method again. After checking the **validate_number_coord** function separately in the *board* module, there was a **ValueError: invalid literal for int() with base 10: ' '**. This is when the method was set up to convert the input into an integer. When the conversion was removed, a **TypeError** was thrown instead, stating that **'<=' not supported between instances of 'int' and 'str'**. Originally, I had the **validate_number_coord** as a simple if/elif statement to catch any invalid inputs. The last elif statement was to catch if any input was not numeric, to ask the player to try again. To fix the bug, I put the function code into a **try except** block. For the elif statement that checks if the input is not numeric, I added a **raise** statement for a **ValueError**, which was then handled in the **except** block. This worked, and when running the full game, did not lead to the game_prompt() function being called again.

## Deployment

The project was deployed to Heroku using the following steps:

1. Sign in to Heroku and access the dashboard
2. In the top right corner, click the "New" dropdown menu and then click "Create new app"
3. Choose a name for your app, then change your region accordingly (for me, it was Europe)
4. Click "Create app"
5. On the next page that loads after clicking "Create app", click "Settings" in the top navigation bar
6. Click on "Reveal Config Vars"
7. Add a new Config Var: type 'PORT' in the 'KEY' section, and type '8000' into the 'VALUE' section, then click "Add"
8. Next, scroll down to the "Buildpack" section and click "Add buildpack"
9. First add "Python", then add "nodejs" - they **must** be in this order
10. In the top navigation bar, click the "Deploy" tab
11. In the "Deployment Method" section, click on *GitHub* to connect to your GitHub account
12. After logging into your GitHub account, search for your GitHub repository name (for this project, it was "sea-conquest")
13. Click on the repository once found to connect it
14. Scroll down to the section "Automatic Deploys" and click on the "Enable Automatic Deploys" button
15. Then underneath, make sure the branch for the project is "main" and click on the "Deploy" button
16. Wait for Heroku to display that the app was deployed successfully

## Credits

- The website used to create the logo art for Sea Conquest was the [Online ASCII Art Creator](https://www.ascii-art-generator.org/)
- The code to clear the python terminal was adapted from [Coding Ninjas](https://www.codingninjas.com/studio/library/how-to-clear-a-screen-in-python)
- The code to use the enumerate function for the ships list was adapted from [Real Python](https://realpython.com/python-enumerate/)

