from flask import jsonify

from src.exceptions.invalidemailexception import InvalidEmailException
from src.exceptions.invalidloginexception import InvalidLoginException
from src.exceptions.invalidnameexception import InvalidNameException
from src.exceptions.invalidphonenumberexception import InvalidPhoneNumberException
from src.exceptions.invalidroleexception import InvalidRoleException
from src.exceptions.useralreadyexistsexception import UserAlreadyExistsException


def register_error_handlers(app):
    @app.errorhandler(UserAlreadyExistsException)
    def handle_user_exists(error):
        response = {
            "success": False,
            "error": {
                "message": error.message,
                "code": error.status_code
            }
        }
        return jsonify(response), error.status_code

    @app.errorhandler(InvalidNameException)
    def handle_invalid_name_exception(error):
        response = {
            "success": False,
            "error": {
                "message": error.message,
                "code": error.status_code
            }
        }
        return jsonify(response), error.status_code

    @app.errorhandler(InvalidRoleException)
    def handle_invalid_role_exception(error):
        response = {
            "success": False,
            "error": {
                "message": error.message,
                "code": error.status_code
            }
        }
        return jsonify(response), error.status_code

    @app.errorhandler(InvalidEmailException)
    def handle_invalid_email_exception(error):
        response = {
            "success": False,
            "error": {
                "message": error.message,
                "code": error.status_code
            }
        }
        return jsonify(response), error.status_code

    @app.errorhandler(InvalidPhoneNumberException)
    def handle_invalid_phone_exception(error):
        response = {
            "success": False,
            "error": {
                "message": error.message,
                "code": error.status_code
            }
        }
        return jsonify(response), error.status_code

    @app.errorhandler(InvalidLoginException)
    def handle_invalid_phone_exception(error):
        response = {
            "success": False,
            "error": {
                "message": error.message,
                "code": error.status_code
            }
        }
        return jsonify(response), error.status_code


    @app.errorhandler(Exception)
    def handle_global_exception(error):
        response = {
            "success": False,
            "error": {
                "message": "Something went wrong",
                "code": 500
            }
        }
        return jsonify(response), 500

