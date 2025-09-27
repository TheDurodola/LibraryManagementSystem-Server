from datetime import datetime
from src.config.config import db

class BorrowRecord(db.Model):
    __tablename__ = "borrow_records"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(17), nullable=False)
    book_title = db.Column(db.String(200), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    borrow_date = db.Column(db.DateTime, default=datetime.now)
    return_date = db.Column(db.DateTime, nullable=True)
    is_returned = db.Column(db.Boolean, default=False)


    def to_dict(self):
        return {
            "id": self.id,
            "isbn13": self.isbn,
            "book_title" : self.book_title,
            "user_email": self.user_email
        }


