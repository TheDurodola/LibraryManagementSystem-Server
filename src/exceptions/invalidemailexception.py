class InvalidEmailException(Exception):
    def __init__(self, message="Invalid Email"):
        self.message = message
        self.status_code = 409
        super().__init__(self.message)