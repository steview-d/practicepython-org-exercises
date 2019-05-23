"""
Not continuing with this as have already done a tic-tac-toe game previously
and I'm just going over the same stuff.
Code from original project pasted below.
"""

"""A simple tic-tac-toe game for 2 players"""

from os import system


class Game:
    """Main class for setting up and running game."""

    def __init__(self, grid, game_active=0):
        """Initialize the variables, and whatnot"""
        self.grid = grid
        self.game_active = game_active

    def draw_screen(self):
        """Method to draw the game screen, inc the tic-tac-toe grid"""
        system('cls')
        dashes = '-----------------'
        print(dashes + '\nTIC-TAC-TOE Game\n' + dashes + '\n')
        print("SCORES\n------")
        print("{} [{}] - {} points\n{} [{}] - {} points".format(p1.name, p1.symbol, p1.score,
                                                                p2.name, p2.symbol, p2.score))
        print("\n-----------------\n")

        self.draw_grid() if self.game_active else draw_menu()
        print('\n')

    def draw_grid(self):
        """Draw the updated 3x3 grid"""

        dashes = '    -------------'
        print('      A   B   C')
        y_axis = 0
        for x in self.grid:
            print(dashes)
            y_axis += 1
            current_line = '  {} | '.format(y_axis)
            for y in x:
                current_line += '{} | '.format(y)
            print(current_line)
        print(dashes)

    def check_win(self, player):
        """Method to check for a winning row of 3.
        Return True OR False depending on outcome"""

        # Generate the string to look for
        looking_for = '{}{}{}'.format(player.symbol, player.symbol, player.symbol)

        # Check Horizontal Lines
        for x in self.grid:
            line_check = ''
            for y in x:
                line_check += y
            if looking_for == line_check:
                return True

        # Check Vertical Lines
        for y in range(0, 3):
            line_check = ''
            for x in self.grid:
                line_check += x[y]
            if looking_for == line_check:
                return True

        # Check Diagonals - long winded way for now....
        line_check = '{}{}{}'.format(self.grid[0][0], self.grid[1][1], self.grid[2][2])
        if looking_for == line_check:
            return True
        line_check = '{}{}{}'.format(self.grid[2][0], self.grid[1][1], self.grid[0][2])
        if looking_for == line_check:
            return True

    def check_draw(self):
        """Checks if all the spaces have been played / filled.
        Should be run after check_win() to ensure a draw result
        isn't called if someone wins on the last move"""
        draw = 0
        for x in self.grid:
            for y in x:
                if ' ' not in y:
                    draw += 1
        if draw == 9:
            return True


class Player:
    """Player class for the game"""

    def __init__(self, name, symbol, score, quit_game=0):
        """Initialize the variables for the player
        Will need to assign a 'X' or 'O'"""
        self.name = name
        self.symbol = symbol
        self.score = score
        self.quit_game = quit_game

    def player_turn(self):
        """Method that allows the player to take a turn"""

        while True:
            move = input("It's {}'s turn - ".format(self.name)).upper()
            # Check to see if player wants to quit
            if move == 'Q' or move == 'QUIT':
                self.quit_game = 1
                break
            # Check to see if input is valid
            if len(move) == 2:
                input_check_letter = move[0]
                input_check_number = move[1]
                if input_check_letter not in 'ABC':
                    print("Invalid move, please try again")
                    continue
                if input_check_number not in '123':
                    print("Invalid move, please try again")
                    continue
            else:
                print("Invalid move, please try again")
                continue

            # Check space isn't already taken
            y_coord = 0
            if move[0] == 'A':
                y_coord = 0
            elif move[0] == 'B':
                y_coord = 1
            elif move[0] == 'C':
                y_coord = 2
            else:
                print("ERROR")
            x_coord = int(move[1]) - 1
            if game.grid[x_coord][y_coord] == ' ':
                game.grid[x_coord][y_coord] = self.symbol
                break
            print("That space has been taken, choose another.")


# Static Functions

def enter_to_continue():
    input('\n(Press Enter To Continue) ')


def draw_menu():
    """Prints the Menu Options"""
    print('MENU OPTIONS\n'
          '------------\n'
          '1. Start New Game\n'
          '2. Reset Scores\n'
          '3. Change Names\n'
          '4. Show Instructions\n'
          '5. Quit Game\n')


def menu():
    choice = input("Choose an option - ")
    if choice == '1':
        game.game_active = 1
    elif choice == '2':
        p1.score = 0
        p2.score = 0
    elif choice == '3':
        p1.name = input('\nEnter a name for player 1: ')
        p2.name = input('Enter a name for player 2: ')
        print('\nPlayer names updated')
        enter_to_continue()
    elif choice == '4':
        print("\nInstructions\n------------\n")
        print('Take turns to enter a O or X into the grid.\n'
              'The first player to get 3 in a row, either\n'
              'horizontally, vertically, or diagonally, wins.\n\n'
              'Take your turn by entering the grid reference\n'
              'of the position you want to play.\n'
              'For example, "A1", or "C2".\n\n'
              'To quit to the main menu at any point during\n'
              'the game, type "QUIT" or "Q".')
        enter_to_continue()
    elif choice == '5':
        print('Thanks for playing!')
        exit()


def reset_game(winner):
    """Increments score, resets grid, and asks to play again"""

    game.grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    while True:
        if winner == 'draw':
            again = input("This game was a draw. Play again? (y/n) ").title()
        else:
            winner.score += 1
            again = input("{} wins this game. Play again? (y/n) ".format(winner.name)).title()
        if again == 'Y':
            return
        if again == 'N':
            game.game_active = 0
            return


# Initialize variables
game = Game([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
p1_name = 'Dave'
p2_name = 'Tester'
p1 = Player(p1_name, 'X', 0)
p2 = Player(p2_name, 'O', 0)
turn = p2

# Main Loop
while True:
    game.draw_screen()
    if game.game_active:
        # Game Loop
        while True:
            if turn == p2:
                turn = p1
            else:
                turn = p2
            turn.player_turn()
            if turn.quit_game == 1:
                turn.quit_game = 0
                game.grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
                game.game_active = 0
                break
            game.draw_screen()
            if game.check_win(turn):
                reset_game(turn)
                break
            if game.check_draw():
                reset_game('draw')
                break
    else:
        menu()

# Notes

# Currently in a working state. Does exactly as it's supposed to.
# Code could be (A LOT) cleaner.
# Plan is to revisit (say 6 months time?) and adjust based on new knowledge & skills.

# Features To Add
# ---------------
# CPU AI - think this one is a (very) way off!
# Text for showing whose turn - choose from random lines instead of always same
# Initializing variables at start - maybe have them read from an .ini file
# ...any more?

# Issues
# ------
# Tried to put [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] into
# a variable to make resetting grid easier, but it wasn't resetting the grid.
# If there was a draw, then a win, no reset after win. NFI why.

# Tried to implement a function to swap players turn between p1/p2 each loop.
# Could not get it to work, currently stuck with ugly looking if / else solution.
# Tried itertools.cycle but program wasn't having it. At all.
