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
   pass


