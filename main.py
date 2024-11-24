from Atonnofpies.class_book import Book
from Atonnofpies.search_engine import find_books

filepath = "library.json"
book1 = Book(1, filepath, "Jane Austen", "Pride and Prejudice", 1813)
book1.process_book()