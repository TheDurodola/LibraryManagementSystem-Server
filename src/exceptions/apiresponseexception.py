class APIResponseException(Exception):
    def __init__(self, message="API Response Error"):
        self.message = message
        self.status_code = 409
        super().__init__(self.message)