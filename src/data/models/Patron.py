from src.data.models.User import User


class Patron(User):
    def __init__(self, user_id, firstname, lastname, password, role, email):
        super().__init__(user_id, firstname, lastname, password, role)