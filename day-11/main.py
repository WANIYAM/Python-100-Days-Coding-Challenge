# 11.Count vowels, consonants, digits, and special characters in a string.

def count_characters(input_string):
    vowels = "aeiouAEIOU"
    digits = "0123456789"

    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_count = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        elif not char.isspace(): 
            special_count += 1

    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Digits:", digit_count)
    print("Special characters:", special_count)


input_str = input("enter string")
count_characters(input_str)
