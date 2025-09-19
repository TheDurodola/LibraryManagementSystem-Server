from src.config.config import db
from src.data.models.user import User

def count() -> int:
    return db.session.query(User).count()


def save( user: User) -> User:
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

def find_all():
    return User.query.all()

def exists(user) -> bool:
    if db.session.query(User).filter_by(email=user.email).first() is not None:
        return True
    else:
        return False


def find_by_email(request) -> User:
    return User.query.filter_by(email=request.email).first()

def delete_by_isbn(isbn: str) -> None:
    user = User.query.filter_by(isbn=isbn).first()
    db.session.delete(user)
    db.session.commit()

def delete_all():
    db.session.query(User).delete()
    db.session.commit()

def delete_user(user: User) -> None:
    db.session.delete(user)
    db.session.commit()


