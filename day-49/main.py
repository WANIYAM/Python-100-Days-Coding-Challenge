# 49.Try-except block to handle multiple exceptions.

class FileTooLargeError(Exception):
    """Custom exception for large files."""
    pass

def read_file(filename):
    try:
        # Simulate checking file size
        size = 105  # Let's say this is MB
        if size > 100:
            raise FileTooLargeError("File size exceeds limit!")

        with open(filename, 'r') as file:
            content = file.read()
            print(content)

    except FileTooLargeError as fte:
        print(f"Custom Error: {fte}")
    except FileNotFoundError:
        print("File not found. Please check the filename.")
    except PermissionError:
        print("You don't have permission to open this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Try running with different filenames
read_file("example.txt")
