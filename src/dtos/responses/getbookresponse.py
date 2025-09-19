class GetBookResponse:
    def __init__(self, book_isbn = None, book_name= None, author_name= None, category_name = None , is_available = None):
        self.book_isbn = book_isbn
        self.book_name = book_name
        self.author_name = author_name
        self.category_name = category_name
        self.is_available = is_available