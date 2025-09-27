import datetime

from sqlalchemy.exc import IntegrityError

from src.config.config import db
from src.data.models.borrowrecord import BorrowRecord
from src.exceptions.unreturnedbookexception import UnreturnedBookException


def count() -> int:
    return db.session.query(BorrowRecord).count()


def save(record: BorrowRecord) -> BorrowRecord:
    if not record.is_returned:
        found_record = BorrowRecord.query.filter_by(isbn=record.isbn, user_email=record.user_email).first()
        if found_record is not None and found_record.is_returned is False:
            raise UnreturnedBookException("Book has not been returned")
        else:
            db.session.add(record)
            db.session.commit()
            return record
    else:
        found_record = BorrowRecord.query.filter_by(isbn=record.isbn, user_email=record.user_email).first()
        db.session.delete(found_record)
        db.session.add(record)
        db.session.commit()
        return record


def return_book(record: BorrowRecord):
    db.session.query(BorrowRecord).filter_by(user_email=record.user_email, isbn=record.isbn).update({"is_returned": True, "return_date": datetime.datetime.now()})
    db.session.commit()


def find_borrowed_book_by_isbn(isbn , user_email):
    return BorrowRecord.query.filter_by(isbn=isbn, user_email= user_email, is_returned=False).first()


def find_record_using_isbn_and_user_email(isbn, user_email):
    found_record = BorrowRecord.query.filter_by(isbn=isbn, user_email=user_email).all()
    return found_record


# def find_record_using_isbn_and_user_email_for_returning(isbn, user_email):
#     found_record = BorrowRecord.query.filter_by(isbn=isbn, user_email=user_email).first()
#     if found_record is False:
#
#
#
#     return found_record

def find_all():
    return BorrowRecord.query.all()





def exists_by_isbn(isbn: str) -> bool:
    if BorrowRecord.query.filter_by(isbn=isbn).first() is not None:
        return True
    else:
        return False


def find_by_isbn(isbn: str) -> BorrowRecord:
    return BorrowRecord.query.filter_by(isbn=isbn).first()


def delete_by_isbn(isbn: str) -> None:
    record = BorrowRecord.query.filter_by(isbn=isbn).first()
    db.session.delete(record)
    db.session.commit()


def delete_all():
    db.session.query(BorrowRecord).delete()
    db.session.commit()


def delete(record: BorrowRecord) -> None:
    db.session.delete(record)
    db.session.commit()


def find_borrowed_books_by_user(user_email):
    return BorrowRecord.query.filter_by(user_email=user_email, is_returned=False).all()