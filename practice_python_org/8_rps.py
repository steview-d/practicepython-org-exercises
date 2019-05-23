"""
Quite possibly the worse implementation of RPS ever, but I'm sick of challenges
asking me to do this and if I have to do one more I'm likely to go and drown
a small animal, so this is as good as it gets.
"""


from random import choice
options = ['R', 'P', 'S']
result = []

def print_choices(p1, cpu):
    if p1 == "R":
        p1_full = "Rock"
    elif p1 == "P":
        p1_full = "Paper"
    else:
        p1_full = "Scissors"
        
    print("You chose {}".format(p1_full))
    print("I chose {}".format(cpu))

while True:
    play_game = input("Do you want to play a game of Rock Paper Scissors? (y/n) > ")
    if play_game.upper() == "N":
        break

    cpu = choice(options)
    p1 = input("Choose either '[R]ock', [P]aper', or '[S]cissors' > ").upper()
    
    print_choices(p1, cpu)
    if p1 == cpu:
        result = "draw"
    elif p1 == "R":
        if cpu == "P":
            result = "lose"
        else:
            result = "win"
    elif p1 == "P":
        if cpu == "S":
            result = "lose"
        else:
            result = "win"
    elif p1 == "S":
        if cpu == "P":
            result = "win"
        else:
            result = "win"
        
        
    if result == "draw":
        print("It's a draw!")
    elif result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")

print("Closing game, goodbye!")