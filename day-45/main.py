# 45.Append data to an existing file.

# Step 1: Create and write initial content
with open("example.txt", "w") as file:
    file.write("Initial line 1\n")
    file.write("Initial line 2\n")

# Step 2: Append new content
with open("example.txt", "a") as file:
    file.write("Appended line 3\n")
    file.write("Appended line 4\n")

# Step 3: Read and display the final content
print("Contents of example.txt after appending:")
with open("example.txt", "r") as file:
    print(file.read())
