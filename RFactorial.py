def factorial(n):
   # n = int(input("Enter a number to find its factorial:"))
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial(10 )