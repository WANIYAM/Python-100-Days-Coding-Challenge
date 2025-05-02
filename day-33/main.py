# 33.Write a Python program to combine two dictionaries.

# Define two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Copy dict1 to avoid modifying the original
combined_dict = dict1.copy()
combined_dict.update(dict2)

print("Combined dictionary:", combined_dict)
