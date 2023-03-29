# Single Player Battleship game!

![Battleship Intro](/images/Battleship%20intro.png)
![Battleship Gameplay](/images/Battleship%20game.png)

Battleships is a Python terminal game which runs on the Code Institute mock terminal on Heroku

Users have 15 missiles to hit 4 ships on a 5X5 grid. Rules of the game can be seen below

The live deployed version on Heroku can be found here:

https://ci-battleship-game.herokuapp.com/

## How to Play
- The aim of the game is to find all of your opponents ships before you
run out of missiles
- You have 4 ships to find with 15 missiles on a 5x5 grid
- Enter a row number between 1-5 , with 1 being the top and 5 being the bottom
- Enter a column between A-E , A being far left and E being the far right
being 4
- If a ship is hit, an 'X' will appear on the board
- If a guess is missed, an '-' will appear on the board
- If you run out of missiles before all the ships are destroyed, you lose
- If you destroy all the ships, you win!

## Features

### Current Features
- Random board generation
    - Ships are randomly placed on the board
    - The player is unable to see where these are located until the end
![Board generation](/images/End%20game.png)
- Accepts user input
- Tracks and displays scores
    - Number of missiles left
    - Number of ships left to hit
- Input validation
    - For rows, only numbers between 1-5 can be entered
    - For columns, only letters A-E can be entered
    - Duplicate guesses are rejected
![Validation](/images/validation.png)

### Future Features
- Play against computer
- Local co-op
- Choose board size
- Choose number of ships
- Have different size ships
- Choose location of ships
- Difficulty settings

## Data Model
- The Board class and the Battleship class was used as the model. The game creates 2 instances of the board to hold the Players board and the Guess board
- The Board class creates and prints the board to the user, and is able to convert letters to numbers
- The Battleship class creates the ships randomly, ask for the user imput and counts how many ships have been hit so the game knows when to end

## Testing
- Manually tested by completing the following:
    - Passed code through a PEP8 linter and confirmed there is no problems 
    - Given invalid inputs to the game
    - Played the game mulitple times to check for issues and to see if the game was beatable
    - Tested throughout in both local terminal and in the deployed Heroku version

### Bugs

#### Solved bugs
- App would not deploy to Heroku. A requirements txt folder was required even though it is empty
- Changed the struture of the player input to a 'While True' structure as empty inputs were being allowed and then crashing the game

#### Remaining bugs
- No remaining bugs

#### Validator testing
- PEP8 

## Deployment 

This project was deployed using the Code Institute's mock terminal for Heroku
- The steps are as followed:
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildpacks to Python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click Deploy

## Credits
- CI tutorials
- CI fpr the deployment terminal 
- YOUTUBE TUTORIAL
- CI tutorials