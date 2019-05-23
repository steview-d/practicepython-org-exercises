"""
Guessing game - but where you think of a number, and
the computer tries to guess it
"""

print("Think of a number between 1 and 100, and I'll guess it!")

while True:
    play_game = input("Ready? (y/n) > ")
    if play_game.lower() == "n":
        print("Thanks for playing!")
        break
    
    lower_range, upper_range = 1, 100
    count = 0
    while True:
        # CPU always guesses the middle number in the given range
        cpu_guess = int((upper_range + lower_range) / 2)
        count += 1
        print("Is your number {}?".format(cpu_guess))
        player_reply = input("[y]es or [n]o? > ")
        
        if player_reply.lower() == 'y':
            print("That was easy! Only took me {} guesses!\nDo you want to play again?".format(count))
            break
        
        while True:
            player_reply = input("Was I too [h]igh, or too [l]ow? > ")
            """
            If the CPU guesses too high, it makes sure the next guess is no
            higher than the last incorrect guess.
            If too low, it makes sure the next guess is no lower than the last
            incorrect guess.
            """
            if player_reply == 'h':
                upper_range = cpu_guess
                break
            elif player_reply == 'l':
                lower_range = cpu_guess
                break
            else:
                print("Your answer made no sense!")