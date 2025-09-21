from flask_login import UserMixin
from datetime import datetime

from flask_login import UserMixin

from src.config.config import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    phone = db.Column(db.String(17), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    code = db.Column(db.String(512), nullable=True)


    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "phone": self.phone,
            "role": self.role,
            "created_at": self.created_at,
        }