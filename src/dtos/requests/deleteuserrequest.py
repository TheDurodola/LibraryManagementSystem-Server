from dataclasses import dataclass


@dataclass
class DeleteUserRequest:
    email : str
    phone : str