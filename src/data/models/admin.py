from werkzeug.security import generate_password_hash, check_password_hash

from src.data.models.user import User


class Admin(User):
    __mapper_args__ = {"polymorphic_identity": "admin"}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = "admin"
        self.code = generate_password_hash("bojIsTheGoat")

    def check_password(self, password):
        return check_password_hash(self.password, password)
