from flask_login import login_user, logout_user, current_user


from src.data.repositories.users import Users
from src.dtos.requests.adduserrequest import AddUserRequest
from src.dtos.responses.adduserresponse import AddUserResponse

from src.utils.mapper import map_add_user_request_to_user, map_user_to_add_user_response
from src.utils.validator import validate_user


class AuthServices:
    @classmethod
    def register_user(cls, request: AddUserRequest) -> AddUserResponse:

        user = map_add_user_request_to_user(request)
        validate_user(user)
        response = map_user_to_add_user_response(Users.save_user(user))
        login_user(user)
        return response



