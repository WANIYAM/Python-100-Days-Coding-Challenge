# 23.Write a function to find GCD of two numbers.

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage:
num1 = 36
num2 = 60
print("GCD of", num1, "and", num2, "is:", find_gcd(num1, num2))
