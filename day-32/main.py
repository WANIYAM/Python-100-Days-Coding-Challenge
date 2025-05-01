# 32.Find frequency of each word in a string.

def word_frequency(text):
    # Convert to lowercase to make counting case-insensitive
    text = text.lower()

    # Remove punctuation (optional, for cleaner word separation)
    import string
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split the string into words
    words = text.split()

    # Create an empty dictionary to store frequencies
    freq = {}

    # Count each word
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq

# Example usage
input_string = "This is a test. This test is only a test."
frequency = word_frequency(input_string)
print(frequency)
