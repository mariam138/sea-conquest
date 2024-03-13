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

