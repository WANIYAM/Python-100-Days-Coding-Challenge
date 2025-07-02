# 68.Find common characters between two strings.

def common_characters(str1, str2):
    return list(set(str1) & set(str2))

# Example usage
s1 = "apple"
s2 = "grape"
print(common_characters(s1, s2))
