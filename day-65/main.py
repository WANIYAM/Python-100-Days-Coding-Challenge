# 65.Use reduce() to multiply all numbers in a list (import functools).

import functools

numbers = [2, 3, 4, 5]

result = functools.reduce(lambda x, y: x * y, numbers)

print("Product of all numbers:", result)
