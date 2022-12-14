import book_pb2;
import json;
import os

FILE_PATH = os.path.dirname(__file__) + '/bookInventory.json'

def retrieveListOfBooks():
    """Retrieves books from book inventory.

    Returns
    ------
    list of books
    """

    with open(FILE_PATH) as file:
        dbBooks = json.load(file)
        books = []
        for book in dbBooks:
            books.append(book_pb2.Book(
                    ISBN=book["ISBN"],
                    title=book["title"],
                    author=book["author"],
                    genre=book["genre"],
                    publishingYear=book["publishingYear"]))
        return books

def storeBooks(books):
    """store books to book inventory.
    """

    dbBooks = json.load(open(FILE_PATH))

    with open(FILE_PATH, "w") as bookInventory:
        for book in books:
            dbBooks.append({
                "ISBN": book.ISBN,
                "title": book.title,
                "author": book.author,
                "genre": book.genre,
                "publishingYear": book.publishingYear
            })

        json.dump(dbBooks, bookInventory, indent=4)