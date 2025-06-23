# 60.Write a class to represent a book (title, author, price).

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

# Example usage:
book1 = Book("To Kill a Mockingbird", "Harper Lee", 12.99)
book1.display_info()
