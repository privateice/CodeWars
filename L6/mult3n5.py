'''
https://www.codewars.com/kata/514b92a657cdc65150000006
If we list all the natural numbers below 10 that are multiples of
	3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples
	of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it
	once.
'''

import math

limit = input("Enter an integer (decimal portions will be truncated): ")
limit = math.trunc(int(limit))
summ = 0

print("Sum of ", end="")
for l in range(limit):
	if (l % 3 == 0) or (l % 5 == 0) or ((l % 3 == 0) and (l % 5 == 0)):
		summ += l
		print(l, end = ' ')

print(summ)		
	