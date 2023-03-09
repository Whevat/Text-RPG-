import time
import os
import random

#Map Variables
x = 1
o = "o"
_ = '_'
left = 5
right = 5

Battle_Chance = 1

#Player Stats
Phealth = 100
Pattack = 5
Pdefense = 0

#Enemy Stats
Ehealth = 50
Eattack = 5
Edefense = 5


print(map)

def Battle():
	print("An Enemy Approaches!")

def other_input():
	p = '.'
	for x in range(4):
		print(x * p, end='\r')
		time.sleep(.5)

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
	if move != "right" or "left":
		other_input()
		