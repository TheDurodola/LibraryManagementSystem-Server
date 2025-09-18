from flask import Blueprint, request, jsonify
from flask_login import logout_user, login_required

from src.dtos.requests.adduserrequest import AddUserRequest
from src.dtos.requests.loginrequest import LoginRequest
from src.services.auth_services import AuthServices

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route('/register', methods=['POST'])
def register_user():
    return jsonify(AuthServices.register_user(AddUserRequest(**request.get_json())).to_dict()), 201


@auth_bp.route('/login', methods=['POST'])
def login_user():
    return jsonify(AuthServices.login_in(LoginRequest(**request.get_json())).to_dict()), 200


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout_user_route():
    logout_user()
    return jsonify({"message": "Logged out"}), 200