"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

def eratosthenes(n):
    primes = [1,2]
    all = []         
    prime = 1  

    i = 3 
    while (i <= n):
        if  i not in all:
            primes.append(i)
            prime += 1
            j = i
            while (j <= (n / i)): 
                all.append(i * j)
                j += 1
        i += 2
    return primes


print eratosthenes(2000000)