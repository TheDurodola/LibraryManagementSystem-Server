from src.config.config import db
from src.data.models.borrowrecord import BorrowRecord


class BorrowRecordsRepository:
    @classmethod
    def save_borrow_record(cls, borrow_record: BorrowRecord):
        db.session.add(borrow_record)
        db.session.commit()
        return borrow_record


    @classmethod
    def get_all_borrow_records(cls):
        return BorrowRecord.query.all()

    @classmethod
    def get_all_unreturned_books(cls):
        return BorrowRecord.query.filter_by(is_returned=False).all()

    @classmethod
    def get_all_unreturned_books_by_user(cls, user_id):
        return BorrowRecord.query.filter_by(borrower_id=user_id, is_returned=False).all()

    @classmethod
    def get_all_returned_books(cls):
        return BorrowRecord.query.filter_by(is_returned=True).all()

    @classmethod
    def return_book(cls, request):
        book = BorrowRecord.query.filter_by(book_isbn= request.bookId,borrower_id=request.userId).first()
        book.is_returned = True
        db.session.commit()





