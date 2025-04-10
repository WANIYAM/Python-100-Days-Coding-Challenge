# 13.Find the length of a string without using len().

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

# Example usage:
my_string =input("enter a string")
print("Length of string:", string_length(my_string))
