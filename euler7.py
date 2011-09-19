"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
import math

def is_prime(n):
    for p in primes:
        if n%p==0:
            return False
    return True
            

n=3
primes=[3]
while len(primes) <= 10000:
    if is_prime(n):
        primes.append(n)
    n+=1

print primes
