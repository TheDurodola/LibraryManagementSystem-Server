from src.config.config import db
from src.data.models.user import User



class Users:
    @classmethod
    def save_user(cls, user: User) -> User:
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def delete_user_by_id(cls, user: User) -> None:
        user_db = db.session.get(User, user.id)

        db.session.delete(user_db)
        db.session.commit()

    @classmethod
    def get_user_by_id(cls, user) -> User:
        return db.session.get(User, user.id)

    @classmethod
    def get_user_by_email(cls, email: str) -> User | None:
        user_email = email
        return db.session.query(User).filter_by(email=user_email).first()

    @classmethod
    def check_table_size(cls) -> int :
        return db.session.query(User).count()

    @classmethod
    def delete_all(cls):
        db.session.query(User).delete()
        db.session.commit()

    @classmethod
    def delete_user(cls, user_email):
        db.session.query(User).filter_by(email=user_email).delete()



