from random import randint
import time


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
    print("1 2 3 4 5")
    for x in range(size):
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
    size = 5
    print("Welcome to Battleships!\n")
    time.sleep(1)
    print("Here are the rules:")
    time.sleep(1)
    print(rules)
    time.sleep(1)
    player_name = input("Please enter your name: \n")
    print(f"\n {player_name}'s Score: 0 ")
    print(" Computer's Score: 0 \n")
    board()



new_game()
