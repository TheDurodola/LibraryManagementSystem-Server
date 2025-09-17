import re

from src.data.repositories.users import Users
from src.exceptions.invalidemailexception import InvalidEmailException
from src.exceptions.invalidnameexception import InvalidNameException
from src.exceptions.invalidphonenumberexception import InvalidPhoneNumberException
from src.exceptions.invalidroleexception import InvalidRoleException
from src.exceptions.useralreadyexistsexception import UserAlreadyExistsException


def validate_user( user):
        if Users.get_user_by_email(user):
            raise UserAlreadyExistsException("User already exists")

        if user.role not in ["librarian", "admin", "patron"]:
            raise InvalidRoleException("Invalid role")

        EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(EMAIL_REGEX, user.email):
            raise InvalidEmailException("Invalid email format")

        NAME_REGEX = r"^[A-Za-z][A-Za-z\s'-]{1,49}$"

        if not re.match(NAME_REGEX, user.firstname):
            raise InvalidNameException("Invalid firstname format")

        if not re.match(NAME_REGEX, user.lastname):
            raise InvalidNameException("Invalid lastname format")

        PHONE_REGEX = r"^(\+?\d{1,3}[- ]?)?(\(?\d{2,4}\)?[- ]?)?\d{3,4}[- ]?\d{4}$"

        if not re.match(PHONE_REGEX, user.phone):
            raise InvalidPhoneNumberException("Invalid phone number format")