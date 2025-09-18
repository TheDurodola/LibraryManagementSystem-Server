from dataclasses import dataclass, Field



class AddUserRequest:
    def __init__(self, firstname=None, lastname=None, email=None, password=None, phone=None, role=None, code=None):
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._password = password
        self._phone = phone
        self._role = role
        self._code = code


    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = value


    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        self._lastname = value


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value


    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value