from random import randint

def compare(guess, answer):
    bullcow = [0, 0]
    for x in range(4):
        if guess[x] == answer[x]:
            bullcow[0] += 1
        else:
            bullcow[1] += 1
    return bullcow


if __name__ == "__main__":
    answer = ''.join([str(randint(0,9)) for x in range(4)])
    count = 0
    while True:
        guess = str(input("Guess the 4 digit number > "))
        if guess == "cheat":
            print(answer)
            continue
        count += 1
        bullcow = compare(guess, answer)
        if bullcow[0] == 4:
            print("Well Done! You have correctly identified all 4 numbers.\nIt took you a total of {} guesses".format(count))
            break
        else:
            print("You have {} bulls and {} cows.".format(bullcow[0], bullcow[1]))

        
