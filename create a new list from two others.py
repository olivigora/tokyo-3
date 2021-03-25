import random
list_a = []
list_b = []
both_lists =[]
for x in range (10):
	list_a.append(random.randrange(1, 27))
	
for y in range (5):
	list_b.append(random.randrange(1, 34))
	
for x in list_a:
	for y in list_b:
		print(list_a)
		print(list_b)
		print(both_lists)