from unittest import TestCase
from src.data.models.book import Book
from src.config.config import db, app
from books import Books

class TestBooks(TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

        db.create_all()
        self.books = Books()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

    def test_save_book(self):
        book = Book()
        book.title = "Book Title"
        book.isbn = "978-0-06-245771-4"
        book.isbn_13 = ""
        book.quantity = 3
        book.genre = "Genre"
        book.desc = "Description"



        saved = self.books.save_book(book)

        self.assertEqual(self.books.check_table_size(), 1)

        self.assertEqual(saved.title, "Book Title")


