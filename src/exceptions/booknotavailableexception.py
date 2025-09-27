class BookNotAvailableException(Exception):
    def __init__(self, message="Book Not Available"):
        self.message = message
        self.status_code = 409
        super().__init__(self.message)
