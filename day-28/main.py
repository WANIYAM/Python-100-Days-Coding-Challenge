# 28.Function to find the largest number from a list.
def find_largest_number(numbers):
    if not numbers:
        return None  # Return None if the list is empty

    largest = numbers[0]  # Assume the first number is the largest initially
    for number in numbers:
        if number > largest:
            largest = number  # Update largest if current number is bigger
    return largest

# Example usage:
my_list = [4, 91, 2, 90, 6]
print("The largest number is:", find_largest_number(my_list))
