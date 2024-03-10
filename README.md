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

## Deployment

## Credits

- The website used to create the logo art for Sea Conquest was the [Online ASCII Art Creator](https://www.ascii-art-generator.org/)
- The code to clear the python terminal was adapted from [Coding Ninjas](https://www.codingninjas.com/studio/library/how-to-clear-a-screen-in-python)

