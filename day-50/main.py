# 50.Write a program to copy content from one file to another.

# Specify the source and destination file names
source_file = "source.txt"
destination_file = "destination.txt"

try:
    # Open the source file in read mode
    with open(source_file, 'r') as src:
        # Read the content of the source file
        content = src.read()

    # Open the destination file in write mode
    with open(destination_file, 'w') as dest:
        # Write the content to the destination file
        dest.write(content)

    print("Content copied successfully from", source_file, "to", destination_file)

except FileNotFoundError:
    print("Error: Source file not found.")
except Exception as e:
    print("An error occurred:", e)
