import time
import os
import random

print("Please only use lower case when playing this game.")

#Map Variables
x = 1
o = "o"
_ = '_'
left = 5
right = 5

#Player Stats
Phealth = 100
Pattack = 20
Pdefense = 2.5
def Player_Stats():
	print(Phealth)
	print(Pattack)
	print(Pdefense)

#Enemy 1 Stats
E1health = 50
E1attack = 5
E1defense = 5
def Enemy_1_Stats():
	print(E1health)
	print(E1attack)
	print(E1defense)

#Enemy 2 Stats
E2health = 25
E2attack = 20
E2defense = 0
def Enemy_2_Stats():
	print(E2health)
	print(E2attack)
	print(E2defense)


print(map)

def Battle():
	global Phealth
	global Pattack
	global Pdefense
	global E2health
	global E2attack
	global E2defense
	global E1attack
	global E1defense
	global E1health
	print("An Enemy Approaches!")
	binput = input(str("What will you do? (Fight or Run) "))
	if binput == "fight":
		print("You decide to fight the Enemy.")
		x = 1
		while x == 1:
			print('Your Stats;')
			Player_Stats()
			print('Their Stats;')
			Enemy_1_Stats()
			finput = input(str("What will you do? (Attack or Defend) "))
			if finput == "attack":
				hit_chance = random.randint(1,3)
				if hit_chance == 1 or 3:
					Edamage = E1defense - Pattack
					E1health = E1health + Edamage
					print(str(Edamage) + " was delt!")
				else:
					print("You Missed!")
				Eattack_chance = random.randint(1,2)
				if Eattack_chance == 1:
					print('The Enemy attacks!')
					ehitchance = random.randint(1,2)
					if ehitchance == 1:
						Pdamage = Pdefense - E1attack
						Phealth = Phealth + Pdamage
						print('You were delt ' + str(Pdamage))
					else:
						print("They missed!")
			if Phealth <= 0:
				x = 0
				print('You have fallen!')
				os.exit()
			elif E1health <= 0:
				x = 0
				print('The enemy has fallen!')

					
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
			Battle_Chance = random.randint(1,2)
			if Battle_Chance == 1:
				Battle()
			else:
				print(map)
	elif right == 0:
		print("Dead End")
	if left != 0:
		if move == "left":
			left = left - 1
			right = right + 1
			map = (left * _ + o + _ * right)
			Battle_Chance = random.randint(1,2)
			if Battle_Chance == 1:
				Battle()
			else:
				print(map)
		elif left == 0:
			print("Dead End")
	if move != "right" or "left":
		other_input()
	if Phealth <= 0:
		x = 0
		print('You Have Died')
		os.exit()