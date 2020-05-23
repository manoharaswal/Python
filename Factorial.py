def factorial(n):
    return 1 if n <= 0 else n * factorial(n - 1)

n = int(input("Enter integer to compute its factorial?: ").strip())
print (str(n) + " != " + str(factorial(n)))
