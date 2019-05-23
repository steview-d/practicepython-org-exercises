import random

word_list = []

with open('assets/words.txt', 'r') as f:
    line = f.readline().strip()
    while line:
        word_list.append(line)
        line = f.readline().strip()

word = random.choice(word_list)
print(word)
print(len(word_list))
