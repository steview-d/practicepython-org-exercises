def fibonacci(num):
    """
    Function that returns a sequence of fibonacci
    numbers of a specified length
    """
    sequence = [1, 1]
    for x in range(num-2):
        sequence.append(sequence[x] + sequence[x+1])
    return sequence


num = int(input("Generate how many fibonacci numbers? > "))
print(fibonacci(num))
