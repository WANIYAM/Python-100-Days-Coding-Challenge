# 69.Check if two strings are anagrams.

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for fair comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Compare sorted versions of both strings
    return sorted(str1) == sorted(str2)

# Example usage:
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
