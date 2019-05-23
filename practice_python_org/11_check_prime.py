def check_prime(num):
    """
    Checks to see if a given integer is a prime number
    Returns true or false
    """
    divisors = []
    for x in range(2, num):
        if (num % x == 0):
            divisors.append(x)
    
    if len(divisors) == 0:
        return True
    else:
        return False
        
        
num = int(input("Please enter a whole number > "))
if check_prime(num):
    print("{} is a prime number".format(num))
else:
    print("{} is not a prime number".format(num))