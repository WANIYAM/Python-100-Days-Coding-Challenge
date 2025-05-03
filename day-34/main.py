# 34.Sort dictionary by values and keys.

my_dict = {'apple': 3, 'banana': 1, 'cherry': 3, 'date': 2}

# Sort by value first, then by key
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: (item[1], item[0])))

print(sorted_dict)
