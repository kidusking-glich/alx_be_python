# library_management.py - Contains the Book and Library classes for the system.

class Book:
    """Represents a book in the library with a title, author, and checkout status."""
    def __init__(self, title, author):
        self.title = title          # Public attribute
        self.author = author        # Public attribute
        self._is_checked_out = False # Private attribute (convention)

    def check_out(self):
        """Marks the book as checked out."""
        # Only check out if it's currently available
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        # Only return if it's currently checked out
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out

class Library:
    """Manages a collection of Book objects."""
    def __init__(self):
        # Private list to store Book instances
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title):
        """Finds a book by title and checks it out if available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' checked out successfully.")
                    return
                else:
                    print(f"Error: '{title}' is already checked out.")
                    return
        print(f"Error: Book with title '{title}' not found.")

    def return_book(self, title):
        """Finds a book by title and marks it as returned."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' returned successfully.")
                    return
                else:
                    print(f"Error: '{title}' was already available.")
                    return
        print(f"Error: Book with title '{title}' not found.")
    
    def list_available_books(self):
        """Lists all books that are currently not checked out."""
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available_count += 1
        
        if available_count == 0:
            print("No books are currently available.")
