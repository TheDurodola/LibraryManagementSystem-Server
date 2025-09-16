from src.config.config import db
from src.data.models.book import Book
from src.data.models.book_reservation import BookReservation
from src.data.models.user import User


class BookReservations(db.Model):
    @classmethod
    def save_book_reservation(cls, book_reservation) -> BookReservation:
        db.session.add(book_reservation)
        db.session.commit()
        return book_reservation

    @classmethod
    def delete_book_reservation_by_userid_isbn(cls, user: User, book: Book) -> None:
        user_id = user.id
        isbn = book.isbn
        book_reservation_db = db.session.get(BookReservation, (user_id, isbn))
        db.session.delete(book_reservation_db)
        db.session.commit()

    @classmethod
    def get_book_reservation_by_userid_isbn(cls, user: User, book: Book) -> BookReservation:
        user_id = user.id
        isbn = book.isbn
        return db.session.get(BookReservation, (user_id, isbn))

    @classmethod
    def check_table_size(cls) -> int :
        return db.session.query(BookReservation).count()

    @classmethod
    def delete_all(cls) -> None:
        db.session.query(BookReservation).delete()
        db.session.commit()