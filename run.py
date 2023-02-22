# from random import randint

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
    print("Welcome to Battleships!\n")
    print("Here are the rules:")
    print(rules)
    player_name = input("Please enter your name: \n")
    print(f"\n {player_name}'s Score: 0 ")
    print(" Computer's Score: 0 \n")
    board()



new_game()
