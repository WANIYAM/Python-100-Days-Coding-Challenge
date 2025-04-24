# 26.Function to find sum and average of list elements.

def sum_and_average(numbers):
    if not numbers:
        return 0, 0  # Return 0, 0 for an empty list
    
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

my_list = [10, 20, 30, 40, 50]
total, avg = sum_and_average(my_list)
print("Sum:", total)
print("Average:", avg)
