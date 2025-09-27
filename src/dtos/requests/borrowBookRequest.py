class BorrowBookRequest:
    def __init__(self, isbn=None, book_title= None, user_email=None):
        self.isbn = isbn
        self.book_title = book_title
        self.user_email = user_email