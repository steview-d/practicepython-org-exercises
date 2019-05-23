from random import randint

a = [randint(1, 21) for x in range(11)]
b = [randint(1, 21) for x in range(15)]

print(sorted(set(a)&set(b)))

# c = [x for x in set(a) if x in set(b)]
# print(c)
