'''
https://www.codewars.com/kata/59ccf051dcc4050f7800008f
DESCRIPTION: Buddy pairs You know what divisors of a number are.
	The divisors of a positive integer n are said to be proper when
	you consider only the divisors other than n itself. In the
	following description, divisors will mean proper divisors. For
	example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.

Let s(n) be the sum of these proper divisors of n. Call buddy two
	positive integers such that the sum of the proper divisors of
	each number is one more than the other number:

(n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

For example 48 & 75 is such a pair:

Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
	Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1 Task
	Given two positive integers start and limit, the function
	buddy(start, limit) should return the first pair (n m) of buddy
	pairs such that n (positive integer) is between start (inclusive)
	and limit (inclusive); m can be greater than limit and has to be
	greater than n 
	
buddy(10, 50) returns [48, 75] 
buddy(48, 50) returns [48, 75]
'''


def findProperDivisors(num):
	temp = []
	for n in range(1, num - 1):
		if not (num % n): temp.append(n)
	#print(temp)
	return temp

def buddy(start, limit):
	for n in range(start, limit):
		proper = findProperDivisors(n)
		sum_n = sum(proper) - 1
		#print(f"Proper divisors of {n} are {proper} s(n) = {sum_n}")
		proper = findProperDivisors(sum_n)
		sum_m = sum(proper) - 1
		#print(f"Proper divisors of {sum_n} are {proper} s(m) = {sum_m}\n")
		if sum_m == n: return [n, sum_n]

#Main Block
print(buddy(10, 50))
print(buddy(48, 50))


