class InvalidQuantityException(Exception):
    def __init__(self, message="Invalid Quantity"):
        self.message = message
        self.status_code = 409
        super().__init__(self.message)