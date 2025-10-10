class Book:
    """
    Base class for all books.
    Attributes: title (str), author (str).
    """
    def __init__(self, title, author):
        """
        Initializes the Book with a title and an author.
        """
        self.title = title
        self.author = author

    def get_details(self):
        """
        Returns the standard details of the book.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class for electronic books, inheriting from Book.
    Additional Attribute: file_size (int).
    """
    def __init__(self, title, author, file_size):
        """
        Initializes EBook, calling the base class constructor first.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        """
        Overrides the base method to include EBook specific details.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class for print books, inheriting from Book.
    Additional Attribute: page_count (int).
    """
    def __init__(self, title, author, page_count):
        """
        Initializes PrintBook, calling the base class constructor first.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        """
        Overrides the base method to include PrintBook specific details.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Class demonstrating composition by managing a collection of Book objects.
    Attributes: books (list of Book, EBook, or PrintBook instances).
    """
    def __init__(self):
        """
        Initializes the Library with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library's collection.
        """
        self.books.append(book)
        # Optional print: print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints the details of all books in the library.
        It relies on the polymorphic behavior of the get_details() method.
        """
        for book in self.books:
            print(book.get_details())

# End of library_system.py
