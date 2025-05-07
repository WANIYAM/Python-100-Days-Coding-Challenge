# 38.Find the difference between two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6, 7}

# Using the '-' operator
difference1 = set1 - set2
print(difference1)  # Output: {1, 2, 5}

# Using the .difference() method
difference2 = set1.difference(set2)
print(difference2)  # Output: {1, 2, 5}
