# 92.Day 92: Dictionary App
# Input word.
# Return meaning (static or using a dictionary package).

from PyDictionary import PyDictionary

def dictionary_app():
    dictionary = PyDictionary()
    
    while True:
        word = input("\nEnter a word (or type 'exit' to quit): ").strip()
        
        if word.lower() == 'exit':
            print("Exiting Dictionary App. Goodbye!")
            break
        
        meaning = dictionary.meaning(word)
        
        if meaning:
            print(f"\nMeanings for '{word}':")
            for part_of_speech, definitions in meaning.items():
                print(f"  {part_of_speech}:")
                for i, definition in enumerate(definitions, 1):
                    print(f"    {i}. {definition}")
        else:
            print(f"No meaning found for '{word}'. Please try another word.")

# Run the app
dictionary_app()
