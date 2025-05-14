# 44.Count number of lines and words in a file.

def count_lines_and_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            
            print(f"Total Lines: {num_lines}")
            print(f"Total Words: {num_words}")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")

# Example usage
count_lines_and_words('example.txt')
