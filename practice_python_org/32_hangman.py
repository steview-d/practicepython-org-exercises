import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def make_word_list(url):
    word_list = []
    with open(url, 'r') as f:
        line = f.readline().strip()
        while line:
            word_list.append(line)
            line = f.readline().strip()
        return word_list



word_list = make_word_list('assets/words.txt')

if __name__ == '__main__':
    print('Welcome To Hangman\n')
    while True:
        word = list(random.choice(word_list).upper())
        correct_letters = []
        guess_list = []
        guess_count = 0
    
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
                
        again = input("Play again? (y/n) > ")
        if again.lower() == 'n':
            print(again)
            break
