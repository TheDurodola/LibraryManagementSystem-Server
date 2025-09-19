from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash

from src.data.repositories.users import *
from src.dtos.requests.adduserrequest import AddUserRequest
from src.dtos.requests.loginrequest import LoginRequest
from src.dtos.responses.adduserresponse import AddUserResponse
from src.dtos.responses.loginresponse import LoginResponse
from src.exceptions.invalidloginexception import InvalidLoginException

from src.utils.mapper import map_add_user_request_to_user, map_user_to_add_user_response, map_user_to_login_response
from src.utils.validator import validate_user


class AuthServices:

    @classmethod
    def register_user(cls, request: AddUserRequest) -> AddUserResponse:
        user = map_add_user_request_to_user(request)
        validate_user(user)
        user.password = generate_password_hash(user.password)
        response = map_user_to_add_user_response(save(user))
        login_user(user)
        return response

    @classmethod
    def login_in(self, request: LoginRequest) -> LoginResponse:
        user = find_by_email(request)
        if user is None:
            raise InvalidLoginException("Email not found")

        if not check_password_hash(user.password, request.password):
            raise InvalidLoginException("Wrong password")
        login_user(user)

        return map_user_to_login_response(user)
