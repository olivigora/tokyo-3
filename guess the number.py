import random
c = 0
a = random.randint(1, 9)
while True:
	print("We selected a random number, can you guess which one it is?")
	usr_comm = input("What is your guess?: ")
	
	if usr_comm == "exit":
		print("Thanks for playing (: ")
		c += 1
		print("You tried", c, "times")
		break
		
	
	ussr_comrade = int(usr_comm)
	
	if ussr_comrade == a:
		print("You got it!")
		c += 1
		break
	
	elif ussr_comrade <= a:
		print("Too low!")
	
	elif ussr_comrade >= a:
		print("Too high!")
	
	c += 1

print("You took only", c, "tries!")