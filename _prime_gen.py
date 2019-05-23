import math

def check_prime(num):
    """
    Checks to see if a given integer is a prime number
    Returns true or false
    """
    for x in range(2, int(math.sqrt(num)+1)):
        if (num % x == 0):
            return False

    return True
        
        
max = int(input("Enter the maximum number to search for primes > "))
primes = []

for x in range(2, max):
    if check_prime(x):
        primes.append(x)

print(primes)
print(len(primes))
    
