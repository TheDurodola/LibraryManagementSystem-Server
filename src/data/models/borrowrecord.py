from datetime import datetime
from src.config.config import db

class BorrowRecord(db.Model):
    __tablename__ = "borrow_records"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_isbn = db.Column(db.String(17), nullable=False)
    borrower_id = db.Column(db.Integer, nullable=False)
    borrow_date = db.Column(db.DateTime, default=datetime.now)
    return_date = db.Column(db.DateTime, nullable=True)
    is_returned = db.Column(db.Boolean, default=False)



