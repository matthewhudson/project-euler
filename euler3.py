"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
def primefactors(x):
    factors = []
    loop = 2
    while loop <= x:
        if x % loop == 0:
            x /= loop
            factors.append(loop)
        else:
            loop += 1
    return factors

print max(primefactors(600851475143))
