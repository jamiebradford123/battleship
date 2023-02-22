from random import randint

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


def new_game():
    """
    Starts a new game. Sets the board sixe and number of ships. Resets the
    scores and randomizes the board
    """
    print("Welcome to Battleships!\n")
    print("Here are the rules:")
    print(rules)


new_game()
