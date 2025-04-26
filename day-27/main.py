# 27.Recursive function to calculate Fibonacci series. 
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example: print the first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i), end=" ")
