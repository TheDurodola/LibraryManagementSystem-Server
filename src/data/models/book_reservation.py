from src.config.config import db

class BookReservation(db.Model):
    __tablename__ = "book_reservations"

    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), primary_key=True)
    isbn = db.Column(db.String(20), db.ForeignKey("books.isbn"), primary_key=True)

    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    is_returned = db.Column(db.Boolean, default=False)

    user = db.relationship("User", back_populates="reservations")
    book = db.relationship("Book", back_populates="reservations")
