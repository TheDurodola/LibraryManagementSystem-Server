class BookAlreadyExistException(Exception):
    def __init__(self, message="Book Already Exists"):
        self.message = message
        self.status_code = 409
        super().__init__(self.message)