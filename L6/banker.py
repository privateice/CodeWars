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
	

