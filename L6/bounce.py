'''DESCRIPTION: A child is playing with a ball on the nth floor of a
	tall building. The height of this floor above ground level, h, is
	known.

He drops the ball out of the window. The ball bounces (for example),
	to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her
	window (including when it's falling and bouncing)?

Three conditions must be met for a valid experiment: Float parameter
	"h" in meters must be greater than 0 Float parameter "bounce"
	must be greater than 0 and less than 1 Float parameter "window"
	must be less than h. If all three conditions above are fulfilled,
	return a positive integer, otherwise return -1.

Note: The ball can only be seen if the height of the rebounding ball
	is strictly greater than the window parameter.'''

import math

def passing(h, b, w):
	if (h <= 0) or not (0 < b < 1) or (w > h):
		return (-1)
	if (w == h): return 0
	passes = 1
	while (h > w):
		h = h * b
		passes += 2
	return passes
	
	
	
#Main block
h = 10 * math.trunc(int(input("What floor is the dropper on? Floor height is 10'. ")))
bounce = float(input("Enter a number between 0 and 1 for the bounciness: "))
window = math.trunc(float(input("Enter an number for the height of the viewing window: ")))

result = passing(h, bounce, window)

if result >= 0:
	print(f"The bouncing ball passes the window {result} times.")
else: print("Error: incorrect parameters, please check what numbers you entered")




