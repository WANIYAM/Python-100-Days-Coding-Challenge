#  31.Find frequency of each character in a string using a dictionary.

# Input string
input_string = "frequency"

# Create an empty dictionary to store character frequencies
char_frequency = {}

# Loop through each character in the string
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Print the frequency of each character
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")
