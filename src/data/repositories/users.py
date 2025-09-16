from src.config.config import db
from src.data.models.user import User



class Users:
    @classmethod
    def save_user(cls, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def delete_user_by_isbn(cls, user: User) -> None:
        user_isbn = user.isbn
        user_db = User.query.get(user_isbn)

        db.session.delete(user_db)
        db.session.commit()

    @classmethod
    def get_user_by_isbn(cls, user_isbn) -> User:
        return User.query.get(user_isbn)


    @classmethod
    def check_table_size(cls) -> int :
        return User.query.count()

