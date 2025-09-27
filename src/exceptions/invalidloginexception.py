class InvalidLoginException(Exception):
    def __init__(self, message="Invalid Login"):
        self.message = message
        self.status_code = 400
        super().__init__(self.message)