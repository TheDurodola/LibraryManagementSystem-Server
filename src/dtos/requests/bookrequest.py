from dataclasses import dataclass


@dataclass
class BookRequest:
    isbn : str
    quantity : int