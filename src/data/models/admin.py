from src.data.models.user import User


class Admin(User):
    __mapper_args__ = {"polymorphic_identity": "admin"}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = "admin"
