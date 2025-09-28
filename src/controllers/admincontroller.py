from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user

from src.dtos.requests.deleteuserrequest import DeleteUserRequest
from src.exceptions.unauthorizedaccessexception import UnauthorizedAccessException
from src.services.admin_services import AdminServices


admin_bp = Blueprint("admin", __name__, url_prefix="/admin")
admin_service = AdminServices()



@admin_bp.route("/users", methods=["GET"])
@login_required
def retrieve_users():
    if current_user.role != "admin":
        raise UnauthorizedAccessException()
    return jsonify(admin_service.get_users()), 200


@admin_bp.route("/patrons", methods=["GET"])
@login_required
def retrieve_all_patrons():
    if current_user.role != "admin":
        raise UnauthorizedAccessException()
    return jsonify(admin_service.get_all_patrons())


@admin_bp.route("/librarian", methods=["GET"])
@login_required
def retrieve_all_librarians():
    if current_user.role != "admin":
        raise UnauthorizedAccessException()
    return jsonify(admin_service.get_all_librarians())


@admin_bp.route("/books", methods=["GET"])
@login_required
def retrieve_all_books():
    if current_user.role != "admin":
        raise UnauthorizedAccessException()
    return jsonify(admin_service.get_all_books())


@admin_bp.route("/avaliablebook", methods=["GET"])
@login_required
def retrieve_all_avaliable_books():
    if current_user.role != "admin":
        raise UnauthorizedAccessException()
    return jsonify(admin_service.get_all_available_books())

@admin_bp.route("/unavaliablebook", methods=["GET"])
@login_required
def retrieve_all_unavaliable_books():
    if current_user.role != "admin":
        raise UnauthorizedAccessException()
    return jsonify(admin_service.get_all_unavailable_books())


@admin_bp.route("/deleteuser", methods=["DELETE"])
@login_required
def delete_user():
    if current_user.role != "admin":
        raise UnauthorizedAccessException()
    data = request.get_json()
    user = DeleteUserRequest(data["email"], data["phone"])
    return jsonify(admin_service.delete_user(user))