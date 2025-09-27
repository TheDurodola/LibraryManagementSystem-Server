from unittest import TestCase

from app import create_app
from src.config.config import db
from src.data.repositories.books import count, find_by_isbn
from src.dtos.requests.addbookrequest import AddBookRequest
from src.dtos.requests.bookrequest import BookRequest
from src.services.librarian_services import LibrarianServices



class TestLibrarianServices(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

        self.service = LibrarianServices()




    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_book(self):
        request = AddBookRequest()
        request.isbn = "9780062457714"
        request.quantity = 1
        request.added_by = 1
        self.service.add_book(request)
        self.assertEqual(count(), 1)


    def test_that_quantity_has_been_increased(self):
        request = AddBookRequest()
        request.isbn = "9780062457714"
        request.quantity = 1
        request.added_by = 1
        self.service.add_book(request)
        self.assertEqual(count(), 1)

        self.assertEqual("The Subtle Art of Not Giving a F**k", self.service.get_all_books()[0]["title"])

        request2 = BookRequest(isbn="9780062457714", quantity=3)

        self.assertIsNotNone(find_by_isbn(request2.isbn))
        self.service.increase_book_quantity(request2)
        self.assertEqual(count(), 1)
        self.assertEqual(find_by_isbn(request2.isbn).quantity, 4)



    def test_get_available_books(self):
        request = AddBookRequest()
        request.isbn = "9780062457714"
        request.quantity = 1
        request.added_by = 1

        self.service.add_book(request)

        request1 = AddBookRequest()
        request1.isbn = "9780062955937"
        request1.quantity = 0
        request1.added_by = 1

        self.service.add_book(request1)

        self.assertEqual(len(self.service.get_all_available_books()), 1)

