# Book Class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


# Patron Class
class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add a new book
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    # Register a new patron
    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"Patron '{patron.name}' registered successfully.")

    # Issue a book
    def issue_book(self, book_id, patron_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    for patron in self.patrons:
                        if patron.patron_id == patron_id:
                            book.available = False
                            patron.borrowed_books.append(book.title)
                            print(f"Book '{book.title}' issued to {patron.name}.")
                            return
                    print("Patron not found.")
                    return
                else:
                    print("Book is not available.")
                    return
        print("Book not found.")

    # Return a book
    def return_book(self, book_id, patron_id):
        for book in self.books:
            if book.book_id == book_id:
                for patron in self.patrons:
                    if patron.patron_id == patron_id:
                        if book.title in patron.borrowed_books:
                            patron.borrowed_books.remove(book.title)
                            book.available = True
                            print(f"Book '{book.title}' returned successfully.")
                            return
                print("Patron not found or book not borrowed.")
                return
        print("Book not found.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.available else "Issued"
            print(f"{book.book_id} - {book.title} by {book.author} ({status})")

    # Display all patrons
    def display_patrons(self):
        print("\nPatrons:")
        for patron in self.patrons:
            print(f"{patron.patron_id} - {patron.name}")
            print("Borrowed Books:", patron.borrowed_books)


# Main Program
library = Library()

# Add Books
book1 = Book(101, "Python Programming", "Guido van Rossum")
book2 = Book(102, "Data Structures", "Mark Allen")

library.add_book(book1)
library.add_book(book2)

# Register Patrons
patron1 = Patron(1, "Naman")
patron2 = Patron(2, "Rahul")

library.register_patron(patron1)
library.register_patron(patron2)

# Display Books
library.display_books()

# Issue Book
library.issue_book(101, 1)

# Display Books
library.display_books()

# Return Book
library.return_book(101, 1)

# Display Books
library.display_books()

# Display Patrons
library.display_patrons()