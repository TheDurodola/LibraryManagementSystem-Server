from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user

from src.dtos.requests.borrowBookRequest import BorrowBookRequest
from src.exceptions.unauthorizedaccessexception import UnauthorizedAccessException
from src.services.patron_services import PatronServices

patron_bp = Blueprint("patron", __name__, url_prefix="/patron")
patron_service = PatronServices()



@patron_bp.route("/book", methods=["GET"])
@login_required
def get_all_available_books():
    if current_user.role != "patron":
        raise UnauthorizedAccessException()
    return jsonify(patron_service.get_all_available_books())


@patron_bp.route("/borrow", methods=["POST"])
@login_required
def borrow_book():
    if current_user.role != "patron":
        raise UnauthorizedAccessException()
    data = request.get_json()
    borrow = BorrowBookRequest()
    borrow.isbn = data["isbn"]
    borrow.user_email = current_user.email
    patron_service.borrow_book(borrow)
    return jsonify({"message": "Book borrowed successfully"})


@patron_bp.route("/borrow", methods=["GET"])
@login_required
def get_all_borrowed_books():
    if current_user.role != "patron":
        raise UnauthorizedAccessException()
    return jsonify(patron_service.get_all_borrowed_books(current_user.email))



@patron_bp.route("/return", methods=["POST"])
@login_required
def return_book():
    if current_user.role != "patron":
        raise UnauthorizedAccessException()
    data = request.get_json()
    borrow = BorrowBookRequest()
    borrow.isbn = data["bookId"]
    borrow.user_email = current_user.email
    patron_service.return_book(borrow)
    return jsonify({"message": "Book returned successfully"})
