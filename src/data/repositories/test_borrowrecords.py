from unittest import TestCase

from app import create_app
from src.config.config import db

from src.data.models.borrowrecord import BorrowRecord
from src.data.repositories.borrowrecords import BorrowRecordsRepository


class Test(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()
        self.borrow = BorrowRecordsRepository()
        self.client = self.app.test_client()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_borrow_records_repository(self):
        bookrecords = BorrowRecord()
        bookrecords.book_isbn = "978-0-06-245771-1"
        bookrecords.borrower_id = 1
        bookrecords.return_date = "2021-01-02"
        self.borrow.save_borrow_record(bookrecords)


    def test_get_borrow_records(self):
        bookrecords = BorrowRecord()
        bookrecords.book_isbn = "978-0-06-245771-1"
        bookrecords.borrower_id = 1
        self.borrow.save_borrow_record(bookrecords)
        bookrecords = BorrowRecord()
        bookrecords.book_isbn = "978-0-06-245771-1"
        bookrecords.borrower_id = 2
        bookrecords.is_returned = True
        self.borrow.save_borrow_record(bookrecords)

        self.assertEqual(len(self.borrow.get_all_unreturned_books()), 1)


