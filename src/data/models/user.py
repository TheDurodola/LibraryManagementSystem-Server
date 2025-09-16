from datetime import datetime
from src.config.config import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(), primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    role = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    __mapper_args__ = {"polymorphic_identity": "user", "polymorphic_on": role}