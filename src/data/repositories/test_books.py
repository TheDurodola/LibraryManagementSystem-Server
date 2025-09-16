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
        self.books.delete_all()

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

        book1 = Book()
        book1.title = "Book Title"
        book1.isbn = "978-0-06-245771-3"
        book1.isbn_13 = "1"
        book1.quantity = 3
        book1.genre = "Genre"
        book1.desc = "Description"

        saved = self.books.save_book(book1)
        self.assertEqual(self.books.check_table_size(), 2)
        self.assertEqual(saved.title, "Book Title")


    def test_delete_book(self):
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
        self.books. delete_book_by_isbn(saved)
        self.assertEqual(self.books.check_table_size(), 0)

    def test_get_book(self):
        book = Book()
        book.title = "Book Title"
        book.isbn = "978-0-06-245771-4"
        book.isbn_13 = ""
        book.quantity = 3
        book.genre = "Genre"
        book.desc = "Description"
        saved = self.books.save_book(book)
        self.assertEqual(self.books.check_table_size(), 1)
        self.assertEqual(saved.title, book.title)
        self.assertEqual(self.books.get_book_by_isbn(saved).title, book.title)



    def test_delete_all_works(self):
        book1 = Book()
        book1.isbn = "978-0-06-245771-4"
        book1.isbn_13 = "1"
        book1.title = "Book Title"
        book1.author = "Author"
        book1.quantity = 3
        book1.genre = "Genre"
        book1.desc = "Description"

        book2 = Book()
        book2.isbn = "978-0-06-245771-2"
        book2.isbn_13 = "2"
        book2.title = "Book Title"
        book2.author = "Author"
        book2.quantity = 3
        book2.genre = "Genre"
        book2.desc = "Description"
        book3 = Book()
        book3.isbn = "978-0-06-245771-1"
        book3.isbn_13 = "3"
        book3.title = "Book Title"
        book3.author = "Author"
        book3.quantity = 3
        book3.genre = "Genre"
        book3.desc = "Description"
        self.books.save_book(book1)
        self.books.save_book(book2)
        self.books.save_book(book3)
        self.assertEqual(self.books.check_table_size(), 3)
        self.books.delete_all()
        self.assertEqual(self.books.check_table_size(), 0)
