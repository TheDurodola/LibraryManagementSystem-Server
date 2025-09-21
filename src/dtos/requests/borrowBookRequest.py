class BorrowBookRequest:
    def __init__(self, bookId=None, userId=None):
        self.bookId = bookId
        self.userId = userId