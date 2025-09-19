import unittest
from unittest import TestCase

from src.data.models.admin import Admin
from src.data.models.librarian import Librarian
from src.data.models.patron import Patron
from app import create_app
from src.config.config import db

from users import Users



class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
        self.users = Users()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_save_all_types_of_user(self):
        self.user = Librarian()
        self.user.id = "1"
        self.user.firstname = "firstname"
        self.user.lastname = "lastname"
        self.user.password = "password"
        self.user.phone = "phone"
        self.user.email = "email1"
        saved = self.users.save_user(self.user)
        self.assertEqual(self.users.check_table_size(), 1)
        self.user1 = Patron()
        self.user1.id = "2"
        self.user1.firstname = "firstname"
        self.user1.lastname = "lastname"
        self.user1.password = "password"
        self.user1.phone = "phone"
        self.user1.email = "email2"

        self.users.save_user(self.user1)
        self.assertEqual(self.users.check_table_size(), 2)
        self.user2 = Admin()
        self.user2.id = "3"
        self.user2.firstname = "firstname"
        self.user2.lastname = "lastname"
        self.user2.password = "password"
        self.user2.phone = "phone"
        self.user2.email = "email3"

        self.users.save_user(self.user2)
        self.assertEqual(self.users.check_table_size(), 3)

    def test_delete_user(self):
        self.user = Librarian()
        self.user.id = "1"
        self.user.firstname = "firstname"
        self.user.lastname = "lastname"
        self.user.password = "password"
        self.user.phone = "phone"
        self.user.email = "email1"
        self.user.role = "admin"
        saved = self.users.save_user(self.user)
        self.assertEqual(self.users.check_table_size(), 1)
        self.users.delete_user_by_id(saved)
        self.assertEqual(self.users.check_table_size(), 0)

