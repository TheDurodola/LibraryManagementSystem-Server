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
        book_isbn = book.isbn
        book_db = Book.query.get(book_isbn)

        db.session.delete(book_db)
        db.session.commit()

    @classmethod
    def get_book_by_isbn(cls, book_isbn) -> Book:
        return Book.query.get(book_isbn)

    @classmethod
    def increase_book_quantity(cls, book: Book, quantity) -> None:
        book_isbn = book.isbn
        book_db = Book.query.get(book_isbn)
        book_db.quantity += quantity

    @classmethod
    def decrease_book_quantity(cls, book_isbn, quantity) -> None:
        book_db = Book.query.get(book_isbn)
        book_db.quantity -= quantity

    @classmethod
    def check_table_size(cls) -> int :
        return Book.query.count()

