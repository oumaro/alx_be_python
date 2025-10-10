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

    def __str__(self):
        """
        Returns the user-friendly string representation of the basic Book object.
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

    def __str__(self):
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

    def __str__(self):
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

    def list_books(self):
        """
        Prints the details of all books in the library using the __str__ method.
        This fixes the previous implementation by relying on the print() function
        to automatically call __str__ on each book object.
        """
        for book in self.books:
            print(book) # print(book) automatically calls book.__str__()
