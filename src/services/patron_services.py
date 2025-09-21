from src.data.models.borrowrecord import BorrowRecord
from src.data.repositories import borrowrecords
from src.data.repositories.books import find_all, find_by_isbn, save
from src.dtos.requests.borrowBookRequest import BorrowBookRequest
from src.exceptions.invalidquantityexception import InvalidQuantityException


class PatronServices:
  def get_all_available_books(self):
    list_of_all_books = find_all()
    list_of_available_books = []
    for book in list_of_all_books:
      if book.quantity > 0:
        list_of_available_books.append(book.to_dict())

    if len(list_of_available_books) == 0:
      raise Exception("No books found")
    return list_of_available_books

  def borrow_book(self, request: BorrowBookRequest):
    book = find_by_isbn(request.bookId)
    if book.quantity <= 0:
      raise InvalidQuantityException("Book is out of stock")
    book.quantity -= 1
    save(book)
    borrow_request = BorrowRecord()
    borrow_request.book_isbn = request.bookId
    borrow_request.borrower_id = request.userId
    borrowrecords.save(borrow_request)




  def return_book(self, request):
    book = find_by_isbn(request.bookId)
    book.quantity += 1
    save(book)
    borrow_request = BorrowRecord()
    borrow_request.book_isbn = request.bookId
    borrow_request.borrower_id = request.userId
    borrowrecords.save(borrow_request)

  def get_all_borrowed_books(self, userid):
    records = borrowrecords.find_all()
    list_of_borrowed_books = []
    for record in records:
      if not record.is_returned:
        if record.borrower_id == userid:
          list_of_borrowed_books.append(record.to_dict())

    if len(list_of_borrowed_books) == 0:
      raise Exception("No borrowed books found")
    return list_of_borrowed_books



