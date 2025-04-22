# 25.Write a function to count words in a string.

def count_words(text):
    words = text.split()
    return len(words)

# Example usage
sample_text = "Agentic AI is transforming Python learning."
word_count = count_words(sample_text)
print("Number of words:", word_count)
