import datetime

from sqlalchemy.exc import IntegrityError

from src.config.config import db
from src.data.models.borrowrecord import BorrowRecord


def count() -> int:
    return db.session.query(BorrowRecord).count()


def save(record: BorrowRecord) -> BorrowRecord:
    if_updateable = BorrowRecord.query.filter_by(book_isbn=record.book_isbn, borrower_id=record.borrower_id).first()

    if if_updateable is not None:
        new_record = if_updateable
        new_record.is_returned = True
        new_record.return_date = datetime.datetime.now()
        db.session.delete(if_updateable)
        db.session.add(new_record)
        db.session.commit()
        return record
    else:
        db.session.add(record)
        db.session.commit()
        return record


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
