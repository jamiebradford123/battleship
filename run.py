import random
import time

rules = """
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

Best of Luck!
"""


def intro():
    """
    Introduction to the game, asks players if they need to see the rules.
    Also contains an input to start the game
    """
    print("Welcome to Battleships!\n")
    show_rules = input("\nWould you like to see the rules? Y/N \n").upper()
    if show_rules == "N":
        print("Good luck!\n")
    elif show_rules == "Y":
        print(rules)
    else:
        print("\nPlease enter Y or N! \n")
        return intro()


class Board:
    """
    Creates and prints the board to the user
    """
    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        """
        Translates the letters users enter to numbers, so the selected column
        letter can be selected
        """
        letters_to_numbers = {
            "A": 0, "B": 1, "C": 2, "D": 3, "E": 4
            }
        return letters_to_numbers

    def print_board(self):
        """
        Prints the board to the user
        """
        print("  A B C D E")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    """
    Creates the ships randomly, ask for the user imput
    and counts how many ships have been hit so the game
    knows when to end
    """
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        """
        Creates the ships randomly on the board
        """
        for i in range(4):
            self.x_row, self.y_column = random.randint(0, 4), \
                random.randint(0, 4)
            # Checks if the position has already been selected, if so run again
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 4), \
                    random.randint(0, 4)
            # Places the ship on the board
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_user_input(self):
        """
        Collects the users input, and validates that their option is valid
        """
        while True:
            x_row = input("Enter the row of the ship (1-5): \n")
            try:
                if int(x_row) in [1, 2, 3, 4, 5]:
                    break
                else:
                    print("Invalid! You must enter a number 1-5")
                    continue
            except Exception:
                print("Invalid! You must enter a number 1-5")
                continue

        while True:
            y_column = input("Enter the col of the ship (A-E): \n").upper()
            try:
                if y_column in ['A', 'B', 'C', 'D', 'E']:
                    break
                else:
                    print("Invalid! You must enter a letter A-E")
                    continue
            except Exception:
                print("Invalid! You must enter a letter A-E")
                continue
        time.sleep(0.5)
        print("Firing now...\n")
        time.sleep(1)
        return int(x_row) - 1, Board.get_letters_to_numbers()[y_column]

    def count_hit_ships(self):
        """
        Counts the number of hit ships
        """
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


def run_game():
    """
    Runs the game
    """
    computer_board = Board([[" "] * 5 for i in range(5)])
    user_guess_board = Board([[" "] * 5 for i in range(5)])
    Battleship.create_ships(computer_board)
    turns = 15
    game_start = input("Press Y to start:  ").upper()
    if game_start == "Y":
        print("Fire away!\n")
    else:
        print("Invalid input")
        return run_game()
    while turns > 0:
        Board.print_board(user_guess_board)
        user_x_row, user_y_column = Battleship.get_user_input(object)
        while user_guess_board.board[user_x_row][user_y_column] == "-" \
                or user_guess_board.board[user_x_row][user_y_column] == "X":
            print("You have already chose this space")
            user_x_row, user_y_column = Battleship.get_user_input(object)
        if computer_board.board[user_x_row][user_y_column] == "X":
            print("You sunk a battleship!")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print("You missed!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print("You sunk all the Battleships! You win")
        else:
            turns -= 1
            print(f"You have {turns} turns remaining")
            print(f"You have hit \
            {Battleship.count_hit_ships(user_guess_board)}out of 4 Ships")
            if turns == 0:
                print("You have run out of missiles. \nGame over!\n")
                Board.print_board(user_guess_board)
                print("\nHere is where the ships were located ")
                Board.print_board(computer_board)
                break
    play_again = input("\nPress Y to play again:  ").upper()
    if play_again == "Y":
        run_game()
    else:
        print("Thanks for playing!")


if __name__ == '__main__':
    intro()
    run_game()
