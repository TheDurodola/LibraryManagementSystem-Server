class LoginRequest:
    def __init__(self, email: str, password: str):
        self.email = email.lower().strip()
        self.password = password