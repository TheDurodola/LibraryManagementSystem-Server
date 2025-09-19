from src.config.config import db
from src.data.models.user import User



class Users:

    def count(self) -> int:
        return db.session.query(User).count()

    def save(self, user: User) -> User:
        if_updateable = User.query.filter_by(id=user.id).first()

        if if_updateable is not None:
            db.session.delete(if_updateable)
            db.session.add(user)
            db.session.commit()
            return user
        else:
            db.session.add(user)
            db.session.commit()
            return user

    def find_all(self):
        return User.query.all()

    def exists_by_isbn(self, isbn: str) -> bool:
        if User.query.filter_by(isbn=isbn).first() is not None:
            return True
        else:
            return False

    def find_by_isbn(self, isbn: str) -> User:
        return User.query.filter_by(isbn=isbn).first()

    def delete_by_isbn(self, isbn: str) -> None:
        user = User.query.filter_by(isbn=isbn).first()
        db.session.delete(user)
        db.session.commit()

    def delete_all(self):
        db.session.query(User).delete()
        db.session.commit()

    def delete_user(self, user: User) -> None:
        db.session.delete(user)
        db.session.commit()


