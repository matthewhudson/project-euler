"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

candidates = [x*y for x in xrange(100, 1000) for y in xrange(100, 1000)]

def reverse_number(num):
	s = ""
	for n in str(num):
		s = n + s
	return int(s)

prospects = [n for n in candidates if n == reverse_number(n)]

print max(prospects)
