num = int(input("Give me a number: "))
x = range(1, num+1)
divisorList = []
for num in x:
	if num % 2 == 0:
		divisorList.append(num)

print("These are the divisors of your number: ")
print(divisorList)