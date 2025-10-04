
# library_management.py

class Book:
    """
    Represents a book in the library with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.
        
        :param title: The title of the book (public).
        :param author: The author of the book (public).
        """
        self.title = title
        self.author = author
        # Private attribute to track availability
        self._is_checked_out = False

    def check_out(self):
        """
        Marks the book as checked out (unavailable).
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            # print(f"'{self.title}' has been checked out.")
            return True
        # else:
            # print(f"'{self.title}' is already checked out.")
        return False

    def return_book(self):
        """
        Marks the book as returned (available).
        """
        if self._is_checked_out:
            self._is_checked_out = False
            # print(f"'{self.title}' has been returned.")
            return True
        # else:
            # print(f"'{self.title}' was not checked out.")
        return False

    def is_available(self):
        """
        Checks the current availability status of the book.
        
        :return: True if the book is not checked out, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Provides a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"

class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        # Private list to store Book instances
        self._books = []

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.
        
        :param book: An instance of the Book class.
        """
        if isinstance(book, Book):
            self._books.append(book)
            # print(f"Added book: {book}")
        else:
            print("Can only add Book objects to the library.")

    def _find_book(self, title):
        """
        Private helper method to find a book by its title.
        
        :param title: The title of the book to find.
        :return: The Book object if found, otherwise None.
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title):
        """
        Finds a book by title and marks it as checked out if available.
        
        :param title: The title of the book to check out.
        """
        book = self._find_book(title)
        if book:
            if book.check_out():
                print(f"Checked out: {title}")
            else:
                print(f"'{title}' is already checked out.")
        else:
            print(f"Book with title '{title}' not found.")

    def return_book(self, title):
        """
        Finds a book by title and marks it as returned (available).
        
        :param title: The title of the book to return.
        """
        book = self._find_book(title)
        if book:
            if book.return_book():
                print(f"Returned: {title}")
            else:
                print(f"'{title}' was already available.")
        else:
            print(f"Book with title '{title}' not found.")

    def list_available_books(self):
        """
        Prints the title and author of all books that are currently available.
        """
        available_books = [book for book in self._books if book.is_available()]
        
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books currently available.")
