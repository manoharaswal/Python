def fibo(n):
	a = 0
	b = 1
	for x in range(n):
		print a,
		c = a + b
		a = b
		b = c

num = int(input("Enter the value of n : "))
fibo(num)
