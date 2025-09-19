from datetime import datetime
from src.config.config import db


class Book(db.Model):
    __tablename__ = 'books'
    isbn = db.Column(db.String(17), primary_key=True)
    isbn_13 = db.Column(db.String(17), unique=True ,nullable=False)
    title = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    added_by = db.Column(db.String(10))
    author = db.Column(db.String(100), nullable=False)

