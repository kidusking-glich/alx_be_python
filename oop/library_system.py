# library_system.py - Defines classes for a Library Management System, 
# demonstrating inheritance (Book -> EBook/PrintBook) and composition (Library).

class Book:
    """
    Base class for all books. Contains common attributes and an __init__ method.
    """
    def __init__(self, title: str, author: str):
        # Public attributes
        self.title = title
        self.author = author

    def __str__(self):
        """String Representation: Returns the basic details of the book."""
        return f"Book: {self.title} by {self.author}"
    
    def get_details(self):
        """Returns the basic details of the book."""
        return str(self)

class EBook(Book):
    """
    Derived class for electronic books. Inherits from Book.
    """
    def __init__(self, title: str, author: str, file_size: int):
        # Call the base class constructor using super()
        super().__init__(title, author)
        # Additional attribute specific to EBook
        self.file_size = file_size
    
    def __str__(self):
        """String Representation: Returns details specific to the EBook."""
        base_details = super().__str__().replace("Book: ", "")
        return f"EBook: {base_details}, File Size: {self.file_size}KB"

    def get_details(self):
        """Returns details specific to the EBook."""
        return str(self)


class PrintBook(Book):
    """
    Derived class for physical print books. Inherits from Book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        # Call the base class constructor
        super().__init__(title, author)
        # Additional attribute specific to PrintBook
        self.page_count = page_count

    def __str__(self):
        """String Representation: Returns details specific to the PrintBook."""
        base_details = super().__str__().replace("Book: ", "")
        return f"PrintBook: {base_details}, Page Count: {self.page_count}"

    def get_details(self):
        """Returns details specific to the PrintBook."""
        return str(self)


class Library:
    """
    Demonstrates composition by managing a collection of Book objects.
    """
    def __init__(self):
        # Private list to store Book, EBook, and PrintBook instances
        self._books = []

    def add_book(self, book: Book):
        """Adds a book instance (of any derived type) to the library."""
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only Book objects (or derived classes) can be added.")

    def list_books(self):
        """Prints the details of every book currently in the library."""
        for book in self._books:
            # Polymorphism: Calls the correct __str__ method (via print or str())
            # based on the book's specific class (Book, EBook, or PrintBook).
            print(book)