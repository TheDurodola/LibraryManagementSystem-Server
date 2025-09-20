import requests


def search_book_by_isbn(isbn: str):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data:", response.status_code)
        return None

    data = response.json()
    if "items" not in data:
        print("No book found for ISBN:", isbn)
        return None

    volume = data["items"][0].get("volumeInfo", {})


    isbn_10, isbn_13 = None, None
    serial_numbers = volume.get("industryIdentifiers", [])
    for item in serial_numbers:
        if item.get("type") == "ISBN_10":
            isbn_10 = item.get("identifier")

    for item in serial_numbers:
        if item.get("type") == "ISBN_13":
            isbn_13 = item.get("identifier")




    return {
        "isbn": isbn_10,
        "isbn_13": isbn_13,
        "title": volume.get("title", "Unknown Title"),
        "genre": (volume.get("categories") or [None])[0],
        "author": (volume.get("authors") or [None])[0]
    }
