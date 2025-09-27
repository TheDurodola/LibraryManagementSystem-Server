from unittest import TestCase

from app import create_app
from src.config.config import db
from src.data.models.borrowrecord import BorrowRecord
from src.data.repositories.books import count
from src.dtos.requests.addbookrequest import AddBookRequest
from src.dtos.requests.adduserrequest import AddUserRequest
from src.dtos.requests.borrowBookRequest import BorrowBookRequest
from src.exceptions.booknotavailableexception import BookNotAvailableException
from src.services.auth_services import AuthServices
from src.services.librarian_services import LibrarianServices
from src.services.patron_services import PatronServices


class TestPatronServices(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.service = PatronServices()
        self.libservice = LibrarianServices()




    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_all_available_books(self):
        self.book = AddBookRequest()
        self.book.isbn = "9780062457714"
        self.book.quantity = 1
        self.book.added_by = 1
        self.libservice.add_book(self.book)
        self.assertEqual(count(), 1)
        self.assertEqual(len(self.service.get_all_available_books()), 1)

    def test_borrow_book(self):
        self.book = AddBookRequest()
        self.book.isbn = "9780062457714"
        self.book.quantity = 1
        self.book.added_by = 1
        self.libservice.add_book(self.book)



        self.assertEqual(count(), 1)
        borrowBookRequest = BorrowBookRequest()
        borrowBookRequest.isbn = "9780062457714"
        borrowBookRequest.user_email = 1
        borrowBookRequest.book_title = "The Subtle Art of Not Giving a F**k"
        self.service.borrow_book(borrowBookRequest)
        self.assertEqual(len(self.service.get_all_borrowed_books("1")), 1)
        with self.assertRaises(BookNotAvailableException):
            self.assertEqual(len(self.service.get_all_available_books()), 0)


    def test_return_book(self):
        self.book = AddBookRequest()
        self.book.isbn = "9780062457714"
        self.book.quantity = 1
        self.book.added_by = 1
        self.libservice.add_book(self.book)

        self.assertEqual(count(), 1)
        borrowBookRequest = BorrowBookRequest()
        borrowBookRequest.isbn = "9780062457714"
        borrowBookRequest.user_email = "1"
        # borrowBookRequest.book_title = "The Subtle Art of Not Giving a F**k"

        self.service.borrow_book(borrowBookRequest)
        self.assertEqual(len(self.service.get_all_borrowed_books("1")), 1)
        with self.assertRaises(BookNotAvailableException):
            self.assertEqual(len(self.service.get_all_available_books()), 0)
        self.service.return_book(borrowBookRequest)
        self.assertEqual(count(), 1)
        with self.assertRaises(BookNotAvailableException):
            self.assertEqual(len(self.service.get_all_borrowed_books("1")), 0)
        self.assertEqual(len(self.service.get_all_available_books()), 1)



    def test_that_user_cant_borrow_more_than_five_different_books_at_once(self):
        self.book = AddBookRequest()
        self.book.isbn = "9780062457714"
        self.book.quantity = 1
        self.book.added_by = 1
        self.libservice.add_book(self.book)
        self.book.isbn = "9780062956569"
        self.book.quantity = 1
        self.book.added_by = 1
        self.libservice.add_book(self.book)
        self.book.isbn = "9781338878929"
        self.book.quantity = 1
        self.book.added_by = 1
        self.libservice.add_book(self.book)
        self.book.isbn = "9780062315007"
        self.book.quantity = 1
        self.book.added_by = 1
        self.libservice.add_book(self.book)
        self.book.isbn = "9780062351562"
        self.book.quantity = 1
        self.book.added_by = 1
        self.libservice.add_book(self.book)
        self.book.isbn = "9780137081073"
        self.book.quantity = 1
        self.book.added_by = 1
        self.libservice.add_book(self.book)
        self.assertEqual(6, count())

        borrowBookRequest = BorrowBookRequest()
        borrowBookRequest.isbn = "9780062457714"
        borrowBookRequest.user_email = "bolajidurodola@gmail.com"
        self.service.borrow_book(borrowBookRequest)

        borrowBookRequest = BorrowBookRequest()
        borrowBookRequest.isbn = "9780062956569"
        borrowBookRequest.user_email = "bolajidurodola@gmail.com"
        self.service.borrow_book(borrowBookRequest)

        borrowBookRequest = BorrowBookRequest()
        borrowBookRequest.isbn = "9781338878929"
        borrowBookRequest.user_email = "bolajidurodola@gmail.com"
        self.service.borrow_book(borrowBookRequest)

        borrowBookRequest = BorrowBookRequest()
        borrowBookRequest.isbn = "9780062315007"
        borrowBookRequest.user_email = "bolajidurodola@gmail.com"
        self.service.borrow_book(borrowBookRequest)

        borrowBookRequest = BorrowBookRequest()
        borrowBookRequest.isbn = "9780062351562"
        borrowBookRequest.user_email = "bolajidurodola@gmail.com"
        self.service.borrow_book(borrowBookRequest)

        borrowBookRequest = BorrowBookRequest()
        borrowBookRequest.isbn = "9780137081073"
        borrowBookRequest.user_email = "bolajidurodola@gmail.com"
        with self.assertRaises(Exception):
            self.service.borrow_book(borrowBookRequest)




