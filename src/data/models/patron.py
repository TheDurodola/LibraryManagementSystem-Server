from src.data.models.user import User


class Patron(User):
    __mapper_args__ = {"polymorphic_identity": "patron"}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = "patron"