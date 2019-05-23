num = int(input("Please enter a whole number > "))

if (num % 4 == 0):
    print ("The number {} is a multiple of 4".format(num))
if (num % 2 == 0):
    print("The number {} is even".format(num))
else:
    print("The number {} is odd".format(num))