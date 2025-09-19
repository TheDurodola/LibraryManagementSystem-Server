from unittest import TestCase

from app import create_app
from src.config.config import db
from src.dtos.requests.addbookrequest import AddBookRequest
from src.services.librarian_services import LibrarianServices


class TestLibrarianServices(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.services = LibrarianServices()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_book(self):
        request = AddBookRequest()
        request.book_isbn = "9780062641540"
        request.quantity = 3

        response = self.services.add_book(request)

        self.assertIsNotNone(response)
        self.assertEqual(response.isbn_13, "9780062641540")
        self.assertEqual(response.quantity, 3)
        self.assertEqual(response.author, "Mark Manson")
        self.assertEqual(response.title, "The Subtle Art of Not Giving a F*ck")

    def test_delete_book(self):
        request = AddBookRequest()
        request.book_isbn = "9780062641540"
        request.quantity = 3

        response = self.services.add_book(request)


        
