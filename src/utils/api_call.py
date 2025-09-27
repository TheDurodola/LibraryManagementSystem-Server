import requests
import os
from dotenv import load_dotenv


from src.exceptions.apiresponseexception import APIResponseException

load_dotenv()
API_KEY = os.getenv("API_KEY")

def search_book_by_isbn(isbn: str):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        raise APIResponseException(f"Google Books API error: {response.status_code} - {response.text}")

    data = response.json()
    if "items" not in data:
        raise APIResponseException(f"No book found for ISBN: {isbn}")

    volume = data["items"][0].get("volumeInfo", {})

    isbn_10, isbn_13 = None, None
    for item in volume.get("industryIdentifiers", []):
        if item.get("type") == "ISBN_10":
            isbn_10 = item.get("identifier")
        elif item.get("type") == "ISBN_13":
            isbn_13 = item.get("identifier")

    return {
        "isbn": isbn_10,
        "isbn_13": isbn_13,
        "title": volume.get("title", "Unknown Title"),
        "genre": (volume.get("categories") or [None])[0],
        "author": (volume.get("authors") or [None])[0],
    }
