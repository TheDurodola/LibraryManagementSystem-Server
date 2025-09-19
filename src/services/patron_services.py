from src.data.models.borrowrecord import BorrowRecord
from src.data.repositories.books import Books
from src.data.repositories.borrowrecords import BorrowRecordsRepository
from src.dtos.requests.borrowBookRequest import BorrowBookRequest



class PatronServices:
    @classmethod
    def borrow_book(cls, request: BorrowBookRequest):
        book = Books.get_book_by_isbn(request.bookId)
        if book.quantity < 1:
            raise Exception("Book quantity is not enough")
        book.quantity = book.quantity - 1
        Books.delete_book_by_isbn(book)
        Books.save_book(book)
        borrow = BorrowRecord()
        borrow.book_isbn = book.isbn
        borrow.borrower_id = request.userId
        BorrowRecordsRepository.save_borrow_record(borrow)


    @classmethod
    def return_book(cls, request: BorrowBookRequest):
        request = Books.get_book_by_isbn(request.bookId)
        request.quantity = request.quantity + 1
        Books.save_book(request)
        BorrowRecordsRepository.return_book(request)





