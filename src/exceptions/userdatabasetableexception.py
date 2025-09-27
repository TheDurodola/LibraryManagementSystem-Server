class UserDatabaseTableException(Exception):
    def __init__(self, message):
        self.message = message
        self.status_code = 409
        super().__init__(self.message)
