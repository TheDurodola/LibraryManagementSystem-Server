from src.config.config import db
from src.data.models.book import Book
from src.exceptions.booknotavailableexception import BookNotAvailableException


def count() -> int:
    return db.session.query(Book).count()


def save(book: Book) -> Book:
    db.session.add(book)
    db.session.commit()
    return book


def find_all_books():
    return Book.query.all()


def exists_by_isbn(isbn: str) -> bool:
    if Book.query.filter_by(isbn=isbn).first() is not None:
        return True
    else:
        return False


def find_by_isbn(isbn: str) -> Book:
    book = db.session.query(Book).filter_by(isbn_13=isbn).first()
    if book:
        return book

    book = Book.query.filter_by(isbn=isbn).first()
    if book:
        return book

    raise BookNotAvailableException("Book not found")


def delete_by_isbn(isbn: str) -> None:
    book = Book.query.filter_by(isbn=isbn).first()
    if book is None:
        book = Book.query.filter_by(isbn_13=isbn).first()
    db.session.delete(book)
    db.session.commit()


def delete_all():
    db.session.query(Book).delete()
    db.session.commit()


def delete_book(book: Book) -> None:
    db.session.delete(book)
    db.session.commit()


def find_all():
    return Book.query.all()
