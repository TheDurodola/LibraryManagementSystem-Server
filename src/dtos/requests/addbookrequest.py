
class AddBookRequest:
    def __init__(self, isbn=None, quantity=None, added_by = None):
        self.isbn = isbn
        self.quantity = quantity
        self.added_by = added_by


