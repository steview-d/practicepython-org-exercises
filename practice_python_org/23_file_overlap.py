with open ('assets/primenumbers.txt', 'r') as f:
    primes = (f.read()).splitlines()
    
with open ('assets/happynumbers.txt', 'r') as f:
    happy = (f.read()).splitlines()

print([i for i in primes if i in happy])

