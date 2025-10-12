# book_class.py - Defines the Book class using Python's magic methods.

class Book:
    """
    A class representing a book with title, author, and year,
    implementing magic methods for initialization, string representation, 
    official representation, and destruction.
    """
    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initializes a new Book instance."""
        self.title = title
        self.author = author
        self.year = year
        # Optional print to show when an object is created (for debugging)
        print(f"Book instance created: {self.title}")

    def __str__(self):
        """
        String Representation: Called by print() and str().
        Returns a user-friendly string format.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Called by repr().
        Returns a string that can be used to recreate the object.
        """
        # Note: self.title and self.author are quoted to ensure the string is valid Python code
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor: Called when the object is about to be destroyed (deleted 
        or garbage collected).
        """
        print(f"Deleting {self.title}")