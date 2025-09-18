class AddUserResponse:
    def __init__(self, firstname=None, email=None, phone=None, role=None):
        self._firstname = firstname
        self._email = email
        self._phone = phone
        self._role = role

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = value



    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value


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


    def to_dict(self):
        return {
            "firstname": self._firstname,
            "email": self._email,
            "phone": self._phone,
            "role": self._role
        }