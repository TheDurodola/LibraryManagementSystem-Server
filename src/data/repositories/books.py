from src.config.config import db
from src.data.models.book import Book



class Books:
    @classmethod
    def save_book(cls, book: Book) -> Book:
        db.session.add(book)
        db.session.commit()
        return book

    @classmethod
    def delete_book_by_isbn(cls, book: Book) -> None:
        book_db = db.session.query(Book).filter_by(isbn=book.isbn).first()

        db.session.delete(book_db)
        db.session.commit()

    @classmethod
    def get_book_by_isbn(cls, book) -> Book:
        return db.session.query(Book).filter_by(isbn=book.isbn).first()


    @classmethod
    def check_table_size(cls) -> int :
        return db.session.query(Book).count()

    @classmethod
    def delete_all(cls) -> None:
        db.session.query(Book).delete()
        db.session.commit()

