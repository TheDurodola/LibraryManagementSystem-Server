class LoginResponse:
    def __init__(self, firstname=None, lastname=None, email=None, role=None, phone=None):
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._role = role
        self._phone = phone


    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def email(self):
        return self._email

    @property
    def role(self):
        return self._role

    @property
    def phone(self):
        return self._phone


    @firstname.setter
    def firstname(self, value):
        self._firstname = value

    @lastname.setter
    def lastname(self, value):
        self._lastname = value

    @email.setter
    def email(self, value):
        self._email = value

    @role.setter
    def role(self, value):
        self._role = value

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_dict(self):
        return {
            "firstname": self._firstname,
            "lastname": self._lastname,
            "email": self._email,
            "role": self._role,
            "phone": self._phone
        }
