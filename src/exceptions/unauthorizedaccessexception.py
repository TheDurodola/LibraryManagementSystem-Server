class UnauthorizedAccessException(ValueError):
    def __init__(self, message="Unauthorized Access"):
        self.message = message
        self.status_code = 409
        super().__init__(self.message)