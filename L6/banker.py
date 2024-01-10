'''
https://www.codewars.com/kata/56445c4755d0e45b8c00010a
DESCRIPTION: John has some amount of money of which he wants to
	deposit a part f0 to the bank at the beginning of year 1. He
	wants to withdraw each year for his living an amount c0.

Here is his banker's plan:

deposit f0 at beginning of year 1 his bank account has an interest
	rate of p percent per year, constant over the years John can
	withdraw each year c0, taking it whenever he wants in the year;
	he must take account of an inflation of i percent per year in
	order to keep his quality of living. i is supposed to stay
	constant over the years. all amounts f0..fn-1, c0..cn-1 are
	truncated by the bank to their integral part Given f0, p, c0, i
	the banker guarantees that John will be able to go on that way
	until the nth year.
'''
import math
c0 = 10000

f0 = 100000
p = 0.01
n = 12
i = 0.011


while n:
	print("n = ", n, "f0 = ", f0)
	f0 = f0 - c0
	c0 = math.ceil(c0 * (1 + i))
	f0 = math.trunc(f0 * (1 + p))
	
	n -= 1
	

