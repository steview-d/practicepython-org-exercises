import random

word_list = []
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('assets/words.txt', 'r') as f:
    line = f.readline().strip()
    while line:
        word_list.append(line)
        line = f.readline().strip()

word = list(random.choice(word_list).upper())

# word = list('SPACES')

correct_letters = []
guess_list = []
guess_count = 0

print('Welcome To Hangman\n')
while True:
    print_word = ''
    for i in word:
        if i in correct_letters:
            print_word += str(i) + ' '
        else:
            print_word += '_ '
    print(print_word)
    print('\nIncorrect guesses so far: {}'.format(guess_count))
    print('Incorrect Letters: ' + '|'.join(guess_list))
    
    if '_' not in print_word:
        print("WIN!")
        break
    
    if guess_count == 6:
        print("LOSE!")
        print("The answer was {}".format(word))
        break
    
    while True:
        guess = str(input("Pick a letter > ")).upper()    
        if guess not in guess_list and len(guess) == 1 and guess in letters:
            break
    
    if guess in word:
        correct_letters.append(guess)
    else:
        guess_list.append(guess)
        guess_count += 1
        
    
    
        
    # if joined guesses string = answer then win, or something

