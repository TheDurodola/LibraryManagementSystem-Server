import re

from werkzeug.security import check_password_hash, generate_password_hash

from src.data.models.admin import Admin
from src.data.repositories.users import *
from src.exceptions.invalidemailexception import InvalidEmailException
from src.exceptions.invalidloginexception import InvalidLoginException
from src.exceptions.invalidnameexception import InvalidNameException
from src.exceptions.invalidphonenumberexception import InvalidPhoneNumberException
from src.exceptions.invalidroleexception import InvalidRoleException
from src.exceptions.useralreadyexistsexception import UserAlreadyExistsException


def validate_user(user):

        existingUser = find_by_email(user)

        if existingUser:
            raise UserAlreadyExistsException("Email already exists")

        if user.role not in ["librarian", "admin", "patron"]:
            raise InvalidRoleException("Invalid role")

        if user.code is not None:
            admin = Admin()
            if check_password_hash(generate_password_hash(user.code), generate_password_hash(admin.code)):
                raise InvalidLoginException("Wrong verification code")

        EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(EMAIL_REGEX, user.email):
            raise InvalidEmailException("Invalid email format")

        NAME_REGEX = r"^[A-Za-z][A-Za-z\s'-]{1,49}$"

        if not re.match(NAME_REGEX, user.firstname):
            raise InvalidNameException("Invalid Firstname format")

        if not re.match(NAME_REGEX, user.lastname):
            raise InvalidNameException("Invalid Lastname format")

        PHONE_REGEX = r"^(\+?\d{1,3}[- ]?)?(\(?\d{2,4}\)?[- ]?)?\d{3,4}[- ]?\d{4}$"

        if not re.match(PHONE_REGEX, user.phone):
            raise InvalidPhoneNumberException("Invalid Phone Number format")