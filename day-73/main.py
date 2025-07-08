# 73.Use random module to generate random numbers.

import random

# Generate a random integer between 1 and 100
random_int = random.randint(1, 100)
print("Random Integer:", random_int)

# Generate a random float between 0 and 1
random_float = random.random()
print("Random Float (0 to 1):", random_float)

# Generate a random float between a custom range
random_uniform = random.uniform(10, 20)
print("Random Float (10 to 20):", random_uniform)

# Pick a random element from a list
items = [10, 20, 30, 40, 50]
random_choice = random.choice(items)
print("Random Choice from List:", random_choice)

# Shuffle a list randomly
random.shuffle(items)
print("Shuffled List:", items)
