class Book:
    """
    A class to model a book with title, author, and publication year,
    implementing essential magic methods for initialization, representation,
    and destruction.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method to initialize a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        # Optional: Print for verification of creation
        # print(f"Book '{self.title}' created.")

    def __str__(self) -> str:
        """
        Returns the user-friendly string representation of the Book object.

        Returns:
            str: A string in the format "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        Returns the official (developer-focused) string representation of the Book object.

        Returns:
            str: A string that can be used to recreate the object, 
                 e.g., "Book('Title', 'Author', 2023)".
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor method called when the object is about to be destroyed (deleted).

        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

# Note: The main.py script is provided for testing and should be separate.
# The code above fulfills the requirement for the book_class.py file.
