from datetime import datetime
from enum import unique

from src.config.config import db


class Book(db.Model):
    __tablename__ = 'books'
    isbn = db.Column(db.String(17), primary_key=True)
    isbn_13 = db.Column(db.String(17), unique=True ,nullable=False)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(1000), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

