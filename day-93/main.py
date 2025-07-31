# 93.Day 93: Random Quote Generator App
# Show a random motivational quote on button click.

import tkinter as tk
import random

# List of motivational quotes
quotes = [
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("Success is not the key to happiness. Happiness is the key to success.", "Albert Schweitzer"),
    ("Push yourself, because no one else is going to do it for you.", "Unknown"),
    ("Dream it. Wish it. Do it.", "Unknown"),
    ("Great things never come from comfort zones.", "Unknown"),
    ("Stay positive. Work hard. Make it happen.", "Unknown"),
]

# Function to generate a random quote
def generate_quote():
    quote, author = random.choice(quotes)
    quote_label.config(text=f'"{quote}"')
    author_label.config(text=f'- {author}')

# GUI Setup
root = tk.Tk()
root.title("Motivational Quote Generator")
root.geometry("500x300")
root.configure(bg="#f0f4f8")

# Quote label
quote_label = tk.Label(root, text="Click the button to get a quote!", wraplength=400,
                       font=("Helvetica", 14), bg="#f0f4f8", justify="center")
quote_label.pack(pady=30)

# Author label
author_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"), bg="#f0f4f8")
author_label.pack()

# Button
quote_button = tk.Button(root, text="Get Quote", command=generate_quote,
                         font=("Helvetica", 12, "bold"), bg="#4caf50", fg="white", padx=20, pady=10)
quote_button.pack(pady=20)

# Run the app
root.mainloop()
