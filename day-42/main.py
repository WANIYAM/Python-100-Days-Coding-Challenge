# 42.Write a list of numbers to a file.

# List of numbers
numbers = [10, 20, 30, 40, 50]

# Open a file in write mode
with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")  # Write each number on a new line
