# 19.Find maximum and minimum in a list without built-in functions.

def find_max_min(lst):
    if not lst:
        return None, None  # Handle empty list

    maximum = lst[0]
    minimum = lst[0]

    for num in lst[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum

# Example usage
numbers = [12, 45, 2, 67, 34, 9]
max_val, min_val = find_max_min(numbers)
print("Maximum:", max_val)
print("Minimum:", min_val)
