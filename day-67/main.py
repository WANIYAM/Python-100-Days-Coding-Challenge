# Check if all elements in a list are unique.
def all_unique(lst):
    return len(lst) == len(set(lst))

# Example usage:
my_list = [1, 2, 3, 4]
print(all_unique(my_list))  # True

my_list = [1, 2, 2, 3]
print(all_unique(my_list))  # False
