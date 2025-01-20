# Dictionary representing a library's book collection
library_books = {
    "1984": {"author": "George Orwell", "copies_available": 4, "genre": "Dystopian"},
    "To Kill a Mockingbird": {"author": "Harper Lee", "copies_available": 2, "genre": "Classic"},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "copies_available": 5, "genre": "Novel"},
    "The Catcher in the Rye": {"author": "J.D. Salinger", "copies_available": 3, "genre": "Fiction"},
    "The Alchemist": {"author": "Paulo Coelho", "copies_available": 6, "genre": "Adventure"},
    "Harry Potter": {"author": "J.K. Rowling", "copies_available": 7, "genre": "Fantasy"},
    "Pride and Prejudice": {"author": "Jane Austen", "copies_available": 3, "genre": "Romance"},
    "The Hobbit": {"author": "J.R.R. Tolkien", "copies_available": 2, "genre": "Fantasy"},
    "Sapiens": {"author": "Yuval Noah Harari", "copies_available": 4, "genre": "History"},
    "Atomic Habits": {"author": "James Clear", "copies_available": 5, "genre": "Self-help"}
}

# Accessing data example
print("Author of '1984':", library_books["1984"]["author"])
print("Copies of 'The Alchemist' available:", library_books["The Alchemist"]["copies_available"])

lc=[item for item in library_books if library_books[item]["genre"]=="Fantasy"]
print(lc)