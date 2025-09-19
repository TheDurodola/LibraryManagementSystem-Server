from unittest import TestCase

from src.config.config import db
from app import create_app
from src.data.repositories.users import Users
from src.dtos.requests.adduserrequest import AddUserRequest
from src.exceptions.useralreadyexistsexception import UserAlreadyExistsException
from src.services.auth_services import AuthServices


class TestAuthServices(TestCase):

    def setUp(self):

        self.app_context = create_app().app_context()
        self.app_context.push()
        self.request_context = create_app().test_request_context()
        self.request_context.push()


        db.create_all()
        Users.delete_all()

        self.request = AddUserRequest()
        self.request.email = "John@gmail.com"
        self.request.firstname = "John"
        self.request.lastname = "Doe"
        self.request.role = "librarian"
        self.request.phone = "2348148260470"
        self.request.password = "<PASSWORD>"
        self.services = AuthServices()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.request_context.pop()
        self.app_context.pop()


    def test_auth_services_register(self):

        saved_user = self.services.register_user(self.request)
        self.assertEqual(saved_user.firstname, "John")
        self.assertEqual(Users.check_table_size(), 1)


        with self.assertRaises(UserAlreadyExistsException):
            self.services.register_user(self.request)
