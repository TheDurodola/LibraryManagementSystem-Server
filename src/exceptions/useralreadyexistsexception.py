class UserAlreadyExistsException(Exception):
    def __init__(self, message="User already exists"):
        self.message = message
        self.status_code = 409
        super().__init__(self.message)
