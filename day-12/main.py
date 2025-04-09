# 12.Check if a string is a palindrome.
def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

input_str = "A man, a plan, a canal: Panama"
if is_palindrome(input_str):
    print("Palindrome")
else:
    print("Not a palindrome")
