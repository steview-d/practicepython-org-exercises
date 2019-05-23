from random import randint

while True:
    play = input("Do you want to play a game? (y/n) > ")
    if play.upper() == "N":
        break
    
    num = randint(1, 9)
    guesses = 0
    
    while True:
        guess = int(input("Pick a number between 1 and 9 > "))
        guesses += 1
        
        if guess == num:
            break
        elif guess > num:
            print("You guessed too high.")
        else:
            print("You guessed too low.")
        
    print("Well Done! You guessed the correct number in {} guesses!".format(guesses))
    
    
    