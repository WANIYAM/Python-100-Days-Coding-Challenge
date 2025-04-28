# Function to check if a string is a palindrome.

def is_palindrome(s):
    # Remove spaces and make lowercase for uniform comparison
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Example usage:
print(is_palindrome("Racecar"))  # True
print(is_palindrome("Hello"))    # False
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
