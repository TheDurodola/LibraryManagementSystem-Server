from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from src.services.librarian_services import LibrarianServices

librarian_bp = Blueprint("librarian", __name__, url_prefix="/librarian")
librarian_service = LibrarianServices()


@librarian_bp.route("/books", methods=["POST"])
@login_required
def add_book():
    data = request.get_json()
    if current_user.role == "librarian":
        librarian_service.add_book(data)
        return None

    else :
        return jsonify({"message": "You are not authorized to perform this action"}), 403







@librarian_bp.route("/bookquatity", methods=["POST"])
@login_required
def increase_book_quatity():
    data = request.get_json()
    librarian_service.add_book_quantity(data)




