# nums = input("Input 3 numbers, separated by a comma, with no spaces > ")
nums = [4,2,5]
highest = 0

for i in nums:
    if (i > highest):
        highest = i

print(highest)