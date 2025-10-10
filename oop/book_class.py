class Book:
    """
    A class to model a book with title, author, and publication year,
    implementing essential magic methods for initialization, representation,
    and destruction.
    """

    def __init__(self, title, author, year):
        """
        Constructor method to initialize a new Book instance.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        Returns the user-friendly string representation of the Book object.
        Expected format: "(title) by (author), published in (year)".
        """
        # Example: 1984 by George Orwell, published in 1949
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official (developer-focused) string representation of the Book object.
        Expected format: f"Book('{self.title}', '{self.author}', {self.year})".
        """
        # Example: Book('1984', 'George Orwell', 1949)
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor method called when the object is about to be destroyed (deleted).
        Prints a message indicating which book is being deleted.
        """
        # Example: Deleting 1984
        print(f"Deleting {self.title}")
