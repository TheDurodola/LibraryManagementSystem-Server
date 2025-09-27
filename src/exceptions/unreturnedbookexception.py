class UnreturnedBookException(Exception):
    def __init__(self, message="Book has already been borrowed by you"):
        self.message = message
        self.status_code = 409
        super().__init__(self.message)