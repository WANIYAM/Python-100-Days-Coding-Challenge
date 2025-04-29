# Function to calculate the power of a number using recursion.

def power(base, exponent):
    # Base case: any number to the power of 0 is 1
    if exponent == 0:
        return 1
    # Recursive case: base^exponent = base * base^(exponent-1)
    return base * power(base, exponent - 1)

# Example usage:
print(power(2, 3))  # Output: 8
