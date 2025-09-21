from src.data.models.user import User

class Librarian(User):
    __mapper_args__ = {"polymorphic_identity": "librarian"}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = "librarian"


