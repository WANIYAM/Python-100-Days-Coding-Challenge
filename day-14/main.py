# 14.Find the second largest number in a list.

def second_largest(numbers):
    first = second = float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

# Get list from user
user_input = input("Enter a list of numbers separated by spaces: ")
num_list = [int(x) for x in user_input.split()]

result = second_largest(num_list)

if result is not None:
    print("Second largest number:", result)
else:
    print("No second largest number found (need at least two distinct values).")
