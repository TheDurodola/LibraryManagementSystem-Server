

from src.data.models.admin import Admin
from src.data.models.librarian import Librarian
from src.data.models.patron import Patron
from src.data.models.user import User
from src.dtos.responses.addbookresponse import AddBookResponse
from src.dtos.responses.adduserresponse import AddUserResponse
from src.dtos.responses.getbookresponse import GetBookResponse
from src.dtos.responses.loginresponse import LoginResponse
from src.exceptions.unauthorizedaccessexception import UnauthorizedAccessException


def map_add_user_request_to_user(request) ->  Admin | Patron | Librarian:
    if request.role == "admin":
        user = Admin()
        user.firstname = request.firstname.capitalize()
        user.lastname = request.lastname.capitalize()
        user.email = request.email.lower()
        user.phone = request.phone
        user.role = request.role
        user.password = request.password
        user.role = request.role
        # if user.code != "bojIsTheGoat":
        #     raise UnauthorizedAccessException("Invalid code. Please contact the system administrator.")
        user.code = request.code
        return user
    if request.role == "patron":
        user = Patron()
        user.firstname = request.firstname
        user.lastname = request.lastname
        user.email = request.email
        user.phone = request.phone
        user.password = request.password
        user.role = request.role
        return user
    if request.role == "librarian":
        user = Librarian()
        user.firstname = request.firstname
        user.lastname = request.lastname
        user.email = request.email
        user.phone = request.phone
        user.role = request.role
        user.password = request.password
        return user
    raise UnauthorizedAccessException("Invalid role. Please contact the system administrator.")


def map_user_to_add_user_response(saved_user: User) -> AddUserResponse:
    response = AddUserResponse()
    response.firstname = saved_user.firstname
    response.lastname = saved_user.lastname
    response.email = saved_user.email
    response.phone = saved_user.phone
    response.role = saved_user.role
    return response


def map_user_to_login_response(user):
    response = LoginResponse()
    response.firstname = user.firstname
    response.lastname = user.lastname
    response.email = user.email
    response.role = user.role
    response.phone = user.phone
    return response



def map_book_to_add_book_response(book) -> AddBookResponse:
    response = AddBookResponse()
    response.title = book.title
    response.isbn = book.isbn
    response.isbn_13 = book.isbn_13
    response.quantity = book.quantity
    response.genre = book.genre
    response.author = book.author
    return response

def map_book_to_get_book_response(book) -> GetBookResponse:
    response = GetBookResponse()
    response.book_name = book.title
    response.book_isbn = book.isbn
    response.author_name = book.author
    if book.quantity > 0:
        response.is_available = True

    else:
        response.is_available = False

    response.category_name = book.genre
    return response

