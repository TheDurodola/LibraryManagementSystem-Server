class InvalidPhoneNumberException(Exception):
    def __init__(self, message="Invalid Phone Number"):
        self.message = message
        self.status_code = 409
        super().__init__(self.message)