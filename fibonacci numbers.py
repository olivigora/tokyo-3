def fibonacci(x):
	a = [1]
	for x in range(x):
		a.append(a[x]+a[x-1])
		print(a)
		
x = int(input("How many Fibonacci numbers do you want?: "))
fibonacci(x)