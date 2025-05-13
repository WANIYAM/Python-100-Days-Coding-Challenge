# 43.Read numbers from a file and calculate their sum.

# Open the file
with open("numbers.txt", "r") as file:
    # Read all lines and convert to integers
    numbers = [int(line.strip()) for line in file]

# Calculate the sum
total = sum(numbers)

# Output the result
print("The sum is:", total)
