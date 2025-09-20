# src/app_factory/create_app.py
from flask import Flask
from flask_cors import CORS
from src.config.config import db, login_manager
from src.controllers.authcontroller import auth_bp
from src.controllers.librariancontroller import librarian_bp
from src.utils.errorhandler import register_error_handlers


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True, origins=["http://localhost:3000"])

    register_error_handlers(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Durodola62@localhost/library'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "super-secret-key"
    app.config['SESSION_COOKIE_SAMESITE'] = "Lax"
    app.config['SESSION_COOKIE_SECURE'] = False

    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(librarian_bp)


    with app.app_context():
        db.create_all()

    return app
