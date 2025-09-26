from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from pyexpat.errors import messages

from src.dtos.requests.addbookrequest import AddBookRequest
from src.dtos.requests.bookrequest import BookRequest
from src.exceptions.unauthorizedaccessexception import UnauthorizedAccessException
from src.services.librarian_services import LibrarianServices

librarian_bp = Blueprint("librarian", __name__, url_prefix="/librarian")
librarian_service = LibrarianServices()


@librarian_bp.route("/book", methods=["POST"])
@login_required
def add_book():
    if current_user.role != "librarian":
        raise UnauthorizedAccessException()
    data = request.get_json()
    add_book_request = AddBookRequest()
    add_book_request.book_isbn = data["book_isbn"]
    add_book_request.quantity = data["quantity"]
    add_book_request.added_by = current_user.email

    if current_user.role == "librarian":
        librarian_service.add_book(add_book_request)
        return jsonify({"message": "Book added successfully"}), 201

    else:
        raise UnauthorizedAccessException()


@librarian_bp.route("/bookquantity", methods=["POST"])
@login_required
def increase_book_quatity():
    if current_user.role != "librarian":
        raise UnauthorizedAccessException()
    data = request.get_json()
    book = BookRequest(data["isbn"], data["quantity"])

    details = librarian_service.increase_book_quantity(book)
    name = details.title
    quantity = details.quantity

    return jsonify({"message": f"{name} quantity increased successfully. New stock quantity is {quantity}"})


@librarian_bp.route("/book", methods=["GET"])
@login_required
def get_all_books():
    if current_user.role != "librarian":
        raise UnauthorizedAccessException()
    return jsonify(librarian_service.get_all_books()), 200
