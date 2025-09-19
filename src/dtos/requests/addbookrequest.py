
class AddBookRequest:
    def __init__(self, book_isbn=None, quantity=None, added_by = None):
        self.book_isbn = book_isbn
        self.quantity = quantity
        self.added_by = added_by


