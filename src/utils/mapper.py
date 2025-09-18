from werkzeug.security import generate_password_hash

from src.data.models.admin import Admin
from src.data.models.librarian import Librarian
from src.data.models.patron import Patron
from src.data.models.user import User
from src.dtos.responses.adduserresponse import AddUserResponse
from src.dtos.responses.loginresponse import LoginResponse


def map_add_user_request_to_user(request) -> None | Admin | Patron | Librarian:
    if request.role == "admin":
        user = Admin()
        user.firstname = request.firstname
        user.lastname = request.lastname
        user.email = request.email
        user.phone = request.phone
        user.role = request.role
        user.password = request.password
        user.role = request.role
        user.code = request.code
        return user
    if request.role == "patron":
        user = Patron()
        user.firstname = request.firstname
        user.lastname = request.lastname
        user.email = request.email
        user.phone = request.phone
        user.role = request.role
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
        user.role = request.role
        return user
    return None


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