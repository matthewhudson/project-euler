"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def euclid(m,n):
    a = (n*n)-(m*m)
    b = 2*(m*n)
    c = (n*n)+(m*m)
    return a,b,c

for m in range(1,22):
    for n in range(1,22):
        if m<n:
            a,b,c=euclid(m,n)
            if (a+b+c)==1000:
                print a*b*c



