class User:
    def __init__(self, user_id = None, firstname= "", lastname = "", password = "", role= ""):
        self._user_id = user_id
        self._firstname = firstname
        self._lastname = lastname
        self._password = password
        self._role = role



    @property
    def id(self):
        return self._user_id

    @id.setter
    def id(self, value):
        self._user_id = value

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
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
