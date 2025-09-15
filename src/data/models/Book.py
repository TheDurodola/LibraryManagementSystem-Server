class Book:
    def __init__(self, book_id, book_name, book_author, book_publisher, isbn, isbn_13, book_quantity):
        self._book_id = book_id
        self._book_name = book_name
        self._book_author = book_author
        self._isbn = isbn
        self._isbn_13 = isbn_13
        self._book_publisher = book_publisher
        self._book_quantity = book_quantity

    @property
    def book_id(self):
        return self._book_id

    @property.setter
    def book_id(self, book_id):
        self._book_id = book_id

    @property
    def book_name(self):
        return self._book_name

    @property.setter
    def book_name(self, book_name):
        self._book_name = book_name

    @property
    def book_author(self):
        return self._book_author

    @property.setter
    def book_author(self, book_author):
        self._book_author = book_author

    @property
    def isbn(self):
        return self._isbn

    @property.setter
    def isbn(self, isbn):
        self._isbn = isbn

    @property
    def isbn_13(self):
        return self._isbn_13

    @property.setter
    def isbn_13(self, isbn_13):
        self._isbn_13 = isbn_13

    @property
    def book_publisher(self):
        return self._book_publisher

    @property.setter
    def book_publisher(self, book_publisher):
        self._book_publisher = book_publisher

    @property
    def book_quantity(self):
        return self._book_quantity

    @property.setter
    def book_quantity(self, book_quantity):
        self._book_quantity = book_quantity




