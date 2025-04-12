# 16.Sum of all elements in a list.
user_input = input("Enter numbers separated by spaces: ")

numbers = list(map(int, user_input.split()))

# Calculate the sum
total = sum(numbers)

print("Sum of all elements:", total)
