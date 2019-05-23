num = int(input("Please enter a whole number > "))

divisors = []

for x in range(1, num + 1):
    if (num % x == 0):
        divisors.append(x)

print(divisors)