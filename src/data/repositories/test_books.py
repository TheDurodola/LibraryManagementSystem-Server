from unittest import TestCase

from app import create_app
from src.config.config import db


from src.data.models.book import Book
from src.data.repositories.books import *


class TestBooks(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.book = Book()
        self.book.isbn = "123456789"
        self.book.isbn_13 = "123456789"
        self.book.title = "test"
        self.book.genre = "test"
        self.book.quantity = 2
        self.book.author = "test"
        self.book.added_by = "test"

        db.create_all()
        

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_save_book(self):
        save(self.book)
        self.assertEqual(count(), 1)

    def test_delete_book_by_book_isbn(self):

        save(self.book)
        delete_by_isbn(self.book.isbn)
        self.assertEqual(count(), 0)

    def test_delete_book(self):

        saved = save(self.book)
        delete_book(saved)
        self.assertEqual(count(), 0)

    def test_that_delete_all(self):
        book1 = Book()
        book1.isbn = "12345678910"
        book1.isbn_13 = "12345678910"
        book1.title = "test"
        book1.genre = "test"
        book1.quantity = 2
        book1.author = "test"
        book1.added_by = "test"

        save(self.book)
        save(book1)
        delete_all()
        self.assertEqual(count(), 0)

    def test_find_all(self):
        save(self.book)
        self.assertEqual(len(find_all()), 1)
