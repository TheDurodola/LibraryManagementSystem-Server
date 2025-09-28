from flask import jsonify

from src.config.config import login_manager
from src.exceptions.apiresponseexception import APIResponseException
from src.exceptions.bookalreadyexistexception import BookAlreadyExistException
from src.exceptions.booknotavailableexception import BookNotAvailableException
from src.exceptions.invalidemailexception import InvalidEmailException
from src.exceptions.invalidloginexception import InvalidLoginException
from src.exceptions.invalidnameexception import InvalidNameException
from src.exceptions.invalidphonenumberexception import InvalidPhoneNumberException
from src.exceptions.invalidquantityexception import InvalidQuantityException
from src.exceptions.invalidroleexception import InvalidRoleException
from src.exceptions.unauthorizedaccessexception import UnauthorizedAccessException
from src.exceptions.unreturnedbookexception import UnreturnedBookException
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

    @app.errorhandler(UnauthorizedAccessException)
    def handle_invalid_phone_exception(error):
        response = {
            "success": False,
            "error": {
                "message": error.message,
                "code": error.status_code
            }
        }
        return jsonify(response), error.status_code

    @app.errorhandler(APIResponseException)
    def handle_api_response_exception(error):
        response = {
            "success": False,
            "error": {
                "message": error.message,
                "code": error.status_code
            }
        }

        return jsonify(response), error.status_code


    @app.errorhandler(UnreturnedBookException)
    def handle_unreturned_book_exception(error):
        response = {
            "success": False,
            "error": {
                "message": error.message,
                "code": error.status_code
            }
        }
        return jsonify(response), error.status_code



    @app.errorhandler(BookNotAvailableException)
    def handle_book_not_available_exception(error):
        response = {
            "success": False,
            "error": {
                "message": error.message,
                "code": error.status_code
            }
        }
        return jsonify(response), error.status_code


    @app.errorhandler(BookAlreadyExistException)
    def handle_global_exception(error):
        response = {
            "success": False,
            "error": {
                "message": error.message,
                "code": 409
            }
        }
        return jsonify(response), 409


    @app.errorhandler(InvalidQuantityException)
    def handle_invalid_quantity_exception(error):
        response = {
            "success": False,
            "error": {
                "message": error.message,
                "code": 400
            }
        }
        return jsonify(response), 400

    @login_manager.unauthorized_handler
    def unauthorized():
        return jsonify({"error": "Unauthorized"}), 401


    # @app.errorhandler(Exception)
    # def handle_global_exception(error):
    #     response = {
    #         "success": False,
    #         "error": {
    #             "message": "Something went wrong. Please contact the administrator.",
    #             "code": 500
    #         }
    #     }
    #     return jsonify(response), 500
