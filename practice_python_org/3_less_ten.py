a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Please enter a whole number > "))

b = [item for item in a if item < 5]
c = [item for item in a if item < num]

print(b)
print(c)

