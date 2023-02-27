from random import randint
import time

def intro():
    """
    Before the game begins screen
    """
    print(
        """
WELCOME TO BATTLESHIPS!\n
"""
    )

    while True:
        try:
            # ask the user for an input
            rules = input(
                    "Would you like to see the rules? Type y for yes or n for no. Enter:\n"
            ).upper()
            # if Y, give the instructions
            if rules == "Y":
                print(
                        """
- The aim of the game is to find all of your opponents ships before they find
yours.
- This game is YOU vs COMPUTER
- Both players have 4 ships to find on a 5x5 grid
- Enter a row number between 0-4 , with 0 being the far left, and right being 4
- Enter a column number between 0-4 , with 0 being the far left, and right
being 4
- If a ship is hit, an '*' will appear on the board
- If a guess is missed, an 'X' will appear on the board
- Each player takes it in turns

Best of Luck!
"""
)
            # if N break the while loop and start the game
            elif rules == "N":
                break
            # otherwise raise an error
            else:
                raise ValueError()
        # if there is an error prompt the user to use a proper command
        except (AttributeError, ValueError):
            print(
                "Please type p to play or i for instructions and press Enter"
            )

rules = """
- The aim of the game is to find all of your opponents ships before they find
yours.
- This game is YOU vs COMPUTER
- Both players have 4 ships to find on a 5x5 grid
- Enter a row number between 0-4 , with 0 being the far left, and right being 4
- Enter a column number between 0-4 , with 0 being the far left, and right
being 4
- If a ship is hit, an '*' will appear on the board
- If a guess is missed, an 'X' will appear on the board
- Each player takes it in turns

Best of Luck!
"""

class Board:
    """
    The board class that will be used for the players and computers board. 
    Sets the size, number of ships, board type (players or comuters). 
    Will add ships and guesses and print the board for each turn.
    """
    def __init__(self, size, num_ships):
        self.size = size
        self.board = [[" " for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.guesses = []
        self.ships = []
    

def board():
    print("Enter the number of rows you would like your game to have:")
    row = int(input("Please enter a number (max:10): "))
    print("Enter the number of columns you would like your game to have:")
    col = int(input("Please enter a number (max:10): "))
    print("1 2 3 4 5")
    for x in range(row):
        print("x "*col)



# def random_point(size):
#     """
#     Returns random integer between 0 and size
#     """

def new_game():
    """
    Starts a new game. Sets the board sixe and number of ships. Resets the
    scores and randomizes the board
    """
    player_name = input("Please enter your name: \n")
    print(f"\n {player_name}'s Score: 0 ")
    print(" Computer's Score: 0 \n")
    board()


intro()
new_game()
