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
    for identifier in volume.get("industryIdentifiers", []):
        if identifier["type"] == "ISBN_10":
            isbn_10 = identifier["identifier"]
        elif identifier["type"] == "ISBN_13":
            isbn_13 = identifier["identifier"]

    return {
        "isbn": isbn_10,
        "isbn13": isbn_13,
        "title": volume.get("title"),
        "description": volume.get("description") or data["items"][0].get("searchInfo", {}).get("textSnippet"),
        "genre": volume.get("categories", [None])[0],
        "author": volume.get("authors", [None])[0]
    }
