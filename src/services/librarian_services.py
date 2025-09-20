from src.data.models.book import Book
from src.data.repositories.books import save, find_by_isbn, find_all
from src.dtos.requests.addbookrequest import AddBookRequest
from src.dtos.requests.bookrequest import BookRequest
from src.dtos.responses.addbookresponse import AddBookResponse
from src.exceptions.invalidquantityexception import InvalidQuantityException
from src.utils.getbookinfo import search_book_by_isbn
from src.utils.mapper import map_book_to_add_book_response


class LibrarianServices:

   def add_book(self, request: AddBookRequest) -> AddBookResponse:
      book = Book()
      apiResponse = search_book_by_isbn(request.book_isbn)
      book.isbn = apiResponse["isbn"]
      book.isbn_13 = apiResponse["isbn_13"]
      book.title = apiResponse["title"]
      book.author = apiResponse["author"]
      book.genre = apiResponse["genre"]
      book.quantity = request.quantity
      book.added_by = request.added_by
      save(book)
      return AddBookResponse(map_book_to_add_book_response(book))


   def increase_book_quantity(self, request:BookRequest) -> None:
      book = find_by_isbn(request.isbn)
      if request.quantity < 0:
         raise InvalidQuantityException("Quantity cannot be negative")
      book.quantity += request.quantity
      save(book)


   def get_all_books(self):
      return find_all()

   def get_all_available_books(self):
      list_of_all_books = find_all()
      list_of_available_books = []
      for book in list_of_all_books:
         if book.quantity > 0:
            list_of_available_books.append(book)
      return list_of_available_books



