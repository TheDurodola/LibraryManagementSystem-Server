from unittest import TestCase

from app import create_app

from src.data.repositories.borrowrecords import *
from src.exceptions.unreturnedbookexception import UnreturnedBookException


class Test(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.bookrecords = BorrowRecord()
        self.bookrecords.isbn = "978-0-06-245771-1"
        self.bookrecords.book_title = "The Subtle Art of Not Giving a F**k"
        self.bookrecords.user_email = "bolajidurodola@gmail.com"
        self.bookrecords.return_date = "2021-01-02"

        db.create_all()
        
        self.client = self.app.test_client()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_borrow_records_repository(self):
        save(self.bookrecords)


    def test_get_records(self):
        save(self.bookrecords)
        bookrecords = BorrowRecord()
        bookrecords.isbn = "978-0-06-245771-1"
        bookrecords.book_title = "The Subtle Art of Not Giving a F**k"
        bookrecords.user_email = "bolajidurodola@gmail.com"
        bookrecords.is_returned = True
        save(bookrecords)
        self.assertEqual(len(find_all()), 1)
        self.assertListEqual(find_all(), [bookrecords])


    def test_that_updated(self):
        saved = save(self.bookrecords)
        self.bookrecords.is_returned = True
        save(self.bookrecords)
        self.assertEqual(count(), 1)

    def test_that_the_same_user_cant_borrow_the_same_book_unless_the_book_is_returned(self):
        saved = save(self.bookrecords)
        with self.assertRaises(UnreturnedBookException):
            save(self.bookrecords)
        self.bookrecords.is_returned = True
        borrows2 = BorrowRecord()
        borrows2.isbn = "978-0-06-245771-1"
        borrows2.book_title = "The Subtle Art of Not Giving a F**k"
        borrows2.user_email = "bolajidurodola@gmail.com"
        save(borrows2)
        self.assertEqual(count(), 2)







