import random

a = random.sample(range(1, 20), 8)
b = random.sample(range(1, 20), 9)
c = [i for i in set(a) if i in b]
result = []
for elem in c:
	if elem not in result:
		result.append(elem)
print(a)
print(b)
print(result)