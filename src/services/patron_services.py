from src.data.models.borrowrecord import BorrowRecord
from src.data.repositories import borrowrecords
from src.data.repositories.books import find_all, find_by_isbn, save
from src.dtos.requests.borrowBookRequest import BorrowBookRequest
from src.exceptions.booknotavailableexception import BookNotAvailableException
from src.exceptions.invalidquantityexception import InvalidQuantityException


def check_request_validity(request):
    book = find_by_isbn(request.isbn)
    validate_request(book, request)

    found_records = borrowrecords.find_record_using_isbn_and_user_email(request.isbn, request.user_email)
    list_of_borrowed_books = []
    for record in found_records:
        if not record.is_returned:
            list_of_borrowed_books.append(record.to_dict())
    if len(list_of_borrowed_books) > 0:
        raise BookNotAvailableException("You have already borrowed this book")
    return book


def validate_request(book, request):
  if book.quantity <= 0:
    raise InvalidQuantityException("Book is out of stock")
  list_of_current_borrowed_books = borrowrecords.find_borrowed_books_by_user(request.user_email)
  if len(list_of_current_borrowed_books) >= 5:
    raise Exception("You can only borrow 5 books at a time")


class PatronServices:
    def get_all_available_books(self):
        list_of_all_books = find_all()
        list_of_available_books = []
        for book in list_of_all_books:
            if book.quantity > 0:
                list_of_available_books.append(book.to_dict())

        if len(list_of_available_books) == 0:
            raise BookNotAvailableException("No books found")
        return list_of_available_books

    def borrow_book(self, request: BorrowBookRequest):
        book = check_request_validity(request)
        if book is None:
            raise BookNotAvailableException("Book not found")
        if book.quantity == 0:
            raise InvalidQuantityException("Book is out of stock")

        book.quantity -= 1
        save(book)
        borrow_request = BorrowRecord()
        borrow_request.isbn = request.isbn
        borrow_request.user_email = request.user_email
        borrow_request.book_title = book.title
        borrowrecords.save(borrow_request)

    def return_book(self, request: BorrowBookRequest):
        validation = borrowrecords.find_borrowed_book_by_isbn(request.isbn, request.user_email)
        if  validation is None:
            raise BookNotAvailableException("You have not borrowed this book")
        book = find_by_isbn(request.isbn)
        if book is None:
            raise BookNotAvailableException("Book not found")

        book.quantity += 1
        save(book)
        borrow_request = BorrowRecord()
        borrow_request.isbn = request.isbn
        borrow_request.user_email = request.user_email
        borrow_request.book_title = request.book_title
        borrowrecords.return_book(borrow_request)

    def get_all_borrowed_books(self, user_email: str):
        records = borrowrecords.find_all()
        list_of_borrowed_books = []
        for record in records:
            if record.user_email == user_email:
                if not record.is_returned:
                    list_of_borrowed_books.append(record.to_dict())

        if len(list_of_borrowed_books) == 0:
            raise BookNotAvailableException("No borrowed books found")
        return list_of_borrowed_books
