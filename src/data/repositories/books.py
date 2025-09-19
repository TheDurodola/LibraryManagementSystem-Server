from src.config.config import db
from src.data.models.book import Book


class BookRepository:
    def count(self) -> int:
        return db.session.query(Book).count()

    def save(self, book: Book) -> Book:
        db.session.add(book)
        db.session.commit()
        return book

    def find_all(self):
        return Book.query.all()

    def exists_by_isbn(self, isbn: str) -> bool:
        if Book.query.filter_by(isbn=isbn).first() is not None:
            return True
        else:
            return False

    def find_by_isbn(self, isbn: str) -> Book:
        return Book.query.filter_by(isbn=isbn).first()

    def delete_by_isbn(self, isbn: str) -> None:
        book = Book.query.filter_by(isbn=isbn).first()
        db.session.delete(book)
        db.session.commit()

    def delete_all(self):
        db.session.query(Book).delete()
        db.session.commit()

    def delete_book(self, book: Book) -> None:
        db.session.delete(book)
        db.session.commit()

