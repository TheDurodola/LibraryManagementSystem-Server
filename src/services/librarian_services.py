from flask_login import current_user

from src.data.models.book import Book
from src.data.repositories.books import Books
from src.dtos.requests.addbookrequest import AddBookRequest
from src.dtos.responses.addbookresponse import AddBookResponse
from src.dtos.responses.getbookresponse import GetBookResponse
from src.exceptions.invalidquantityexception import InvalidQuantityException
from src.utils.getbookinfo import search_book_by_isbn
from src.utils.mapper import map_book_to_add_book_response, map_book_to_get_book_response




class LibrarianServices:
    @classmethod
    def add_book(cls, request : AddBookRequest) -> AddBookResponse:
        list_of_book_info = search_book_by_isbn(request.book_isbn)
        book = Book()
        book.title = list_of_book_info["title"]
        book.isbn = list_of_book_info["isbn"]
        book.isbn_13 = list_of_book_info["isbn13"]
        book.quantity = request.quantity
        book.genre = list_of_book_info["genre"]
        book.author = list_of_book_info["author"]
        book.added_by = request.added_by
        return map_book_to_add_book_response(Books.save_book(book))


    @classmethod
    def get_book_by_isbn(cls, isbn: str) -> GetBookResponse:
        book = Books.get_book_by_isbn(isbn)
        return map_book_to_get_book_response(book)


    @classmethod
    def add_book_quantity(cls, addToBookQuantityRequest) -> None:
        book = Books.get_book_by_isbn(addToBookQuantityRequest.isbn)
        if addToBookQuantityRequest.quantity < 0:
            raise InvalidQuantityException("Quantity cannot be negative")
        book.quantity += addToBookQuantityRequest.quantity
        Books.delete_book_by_isbn(book)
        Books.save_book(book)













