class AddBookResponse:
    def __init__(self, title=None, isbn=None, isbn_13=None, author=None, genre=None, quantity=None):
        self._title = title
        self._isbn = isbn
        self._isbn_13 = isbn_13
        self._author = author
        self._genre = genre
        self._quantity = quantity



    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @property
    def isbn_13(self):
        return self._isbn_13

    @isbn_13.setter
    def isbn_13(self, value):
        self._isbn_13 = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

