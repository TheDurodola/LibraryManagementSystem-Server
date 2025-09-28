from src.config.config import db
from src.data.models.user import User
from src.dtos.requests.deleteuserrequest import DeleteUserRequest


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
    return User.query.filter_by(email=request.email.lower().strip()).first()

def delete_by_email_and_phone(request: DeleteUserRequest) -> bool:
    user = User.query.filter_by(email=request.email, phone = request.phone).first()
    if user is None:
        return False
    db.session.delete(user)
    db.session.commit()
    return True


def delete_all():
    db.session.query(User).delete()
    db.session.commit()

def delete_user(user: User) -> None:
    db.session.delete(user)
    db.session.commit()


