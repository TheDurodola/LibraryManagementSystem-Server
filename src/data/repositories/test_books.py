from unittest import TestCase

from src.config.config import db
from src.data.models.book import Book
from app import create_app
from books import Books


class TestBooks(TestCase):
    def setUp(self):

        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()


        db.create_all()


        self.books = Books()
        self.books.delete_all()


        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_save_book(self):
        book = Book(
            title="Book Title",
            isbn="978-0-06-245771-1",
            author="Mark Manson",
            isbn_13="1",
            quantity=3,
            genre="Genre",

        )
        saved = self.books.save_book(book)
        self.assertEqual(self.books.check_table_size(), 1)
        self.assertEqual(saved.title, "Book Title")

    def test_delete_book(self):
        book = Book()

        book.title = "Book Title"
        book.isbn = "978-0-06-245771-3"
        book.isbn_13 = "3"
        book.quantity = 3
        book.author = "Mark Manson"
        book.genre = "Genre"


        saved = self.books.save_book(book)
        self.assertEqual(self.books.check_table_size(), 1)
        self.books.delete_book_by_isbn(saved)
        self.assertEqual(self.books.check_table_size(), 0)

    def test_get_book(self):
        book = Book()

        book.title = "Book Title"
        book.isbn = "978-0-06-245771-4"
        book.isbn_13 = "4"
        book.quantity = 3
        book.genre = "Genre"

        book.author = "Mark Manson"
        saved = self.books.save_book(book)
        self.assertEqual(self.books.get_book_by_isbn(saved).title, book.title)

    def test_delete_all_works(self):
        book1 = Book(isbn="978-0-06-245771-5", isbn_13="5", title="Book Title", quantity=3, genre="Genre",
                     )
        book2 = Book(isbn="978-0-06-245771-6", isbn_13="6", title="Book Title", quantity=3, genre="Genre",
                    )
        book3 = Book(isbn="978-0-06-245771-7", isbn_13="7", title="Book Title", quantity=3, genre="Genre",
                     )
        book1.author = "Mark Manson"
        book2.author = "Mark Manson"
        book3.author = "Mark Manson"

        self.books.save_book(book1)
        self.books.save_book(book2)
        self.books.save_book(book3)
        self.assertEqual(self.books.check_table_size(), 3)
        self.books.delete_all()
        self.assertEqual(self.books.check_table_size(), 0)
