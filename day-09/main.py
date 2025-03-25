# Sum of digits of a number.


def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# Example usage
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
