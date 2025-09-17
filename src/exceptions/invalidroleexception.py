class InvalidRoleException(ValueError):
    def __init__(self, message="Invalid Role"):
        self.message = message
        self.status_code = 409
        super().__init__(self.message)