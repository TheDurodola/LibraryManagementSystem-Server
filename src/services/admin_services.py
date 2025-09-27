from src.data.repositories import books
from src.data.repositories.users import find_all, delete_by_email_and_phone
from src.dtos.requests.deleteuserrequest import DeleteUserRequest
from src.exceptions.booknotavailableexception import BookNotAvailableException
from src.exceptions.userdatabasetableexception import UserDatabaseTableException


class AdminServices:
    def get_users(self):
        data =  find_all()
        list_of_users = []
        for user in data:
            list_of_users.append(user.to_dict())

        if len(list_of_users) == 0:
            raise UserDatabaseTableException("No users found")
        return list_of_users


    def get_all_patrons(self):
        list_of_users = find_all()
        list_of_patrons = []
        for user in list_of_users:
            if user.role == "patron":
                list_of_patrons.append(user.to_dict())

        if len(list_of_patrons) == 0:
            raise UserDatabaseTableException("No patrons found")
        return list_of_patrons

    def get_all_books(self):
        list_of_all_books = books.find_all()
        list_of_books = []
        for book in list_of_all_books:
            list_of_books.append(book.to_dict())

        if len(list_of_books) == 0:
            raise BookNotAvailableException("No books found")
        return list_of_books


    def get_all_librarians(self):
        list_of_users = find_all()
        list_of_librarians = []
        for user in list_of_users:
            if user.role == "librarian":
                list_of_librarians.append(user.to_dict())

        if len(list_of_librarians) == 0:
            raise UserDatabaseTableException("No librarians found")
        return list_of_librarians


    def get_all_available_books(self):
        list_of_all_books = books.find_all()
        list_of_available_books = []
        for book in list_of_all_books:
            if book.quantity > 0:
                list_of_available_books.append(book.to_dict())

        if len(list_of_available_books) == 0:
            raise BookNotAvailableException("No books found")
        return list_of_available_books

    def delete_user(self, request: DeleteUserRequest):
        deleted = delete_by_email_and_phone(request)
        if deleted:
            return {"message": "User deleted successfully"}
        else:
            raise UserDatabaseTableException("User not found")

    def get_all_unavailable_books(self):
        list_of_all_books = books.find_all()
        list_of_unavailable_books = []
        for book in list_of_all_books:
            if book.quantity == 0:
                list_of_unavailable_books.append(book.to_dict())

        if len(list_of_unavailable_books) == 0:
            raise BookNotAvailableException("No books found")

        return list_of_unavailable_books
