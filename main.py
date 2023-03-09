import time
import os

x = 1
o = "o"
_ = '_'
left = 5
right = 5

print(map)

while x == 1: 
	map = (left * _ + o + _ * right)

	time.sleep(1)
	
	move = input(str("Where? "))
	
	if right != 0:
		if move == "right":
			left = left + 1
			right = right - 1
			map = (left * _ + o + _ * right)
			print(map)
	elif right == 0:
		print("Dead End")
	if left != 0:
		if move == "left":
			left = left - 1
			right = right + 1
			map = (left * _ + o + _ * right)
			print(map)
		elif left == 0:
			print("Dead End")