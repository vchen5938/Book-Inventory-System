from concurrent import futures
import logging

import grpc
import inventory_pb2
import inventory_pb2_grpc
import inventoryService_pb2
import inventoryService_pb2_grpc
import json

class InventoryService(inventoryService_pb2_grpc.InventoryServiceServicer):
    
    # Validate book input
    def validateInput(self, request):
        if request.ISBN == "":
            return (False, "Book's ISBN is invalid!!!")
        elif request.title == "":
            return (False, "Book's title is invalid!!!")
        elif request.author == "":
            return (False, "Book's author is invalid!!!")
        elif request.genre <= 0 or request.genre >= 5:
            return (False, "Book's genre not available!!!")
        elif request.publishingYear == 0:
            return (False, "Book's publishing year is invalid!!!")
        else:
            return (True, "Book is valid.")

    # Create a book and add it to database
    def CreateBook(self, request, context):
        valid, message = self.validateInput(request)

        if not valid:
            bookResponseStatus = inventory_pb2.BookResponseStatus()
            bookResponseStatus.statusCode = inventory_pb2.FAILURE
            bookResponseStatus.message = message
            return bookResponseStatus
        
        file = open('bookInventory.json')
        books = json.load(file)

        # check for duplicate ISBNs
        for book in books:
            if book["ISBN"] == request.ISBN:
                bookResponseStatus = inventory_pb2.BookResponseStatus()
                bookResponseStatus.statusCode = inventory_pb2.FAILURE
                bookResponseStatus.message = "A book with the same ISBN has been created!!!"
                return bookResponseStatus

        # create the new book and add it to bookInventory
        with open("bookInventory.json", "w") as outfile:
            book = {
            "ISBN": request.ISBN,
            "title": request.title,
            "author": request.author,
            "genre": request.genre,
            "publishingYear": request.publishingYear
            }
            books.append(book)

            json.dump(books, outfile, indent=4)
        
        bookResponseStatus = inventory_pb2.BookResponseStatus()
        bookResponseStatus.statusCode = inventory_pb2.SUCCESS
        bookResponseStatus.message = "Book created successfully!!!"
        return bookResponseStatus
    
    # Get book details if it exists in the database
    def GetBook(self, request, context):
        file = open('bookInventory.json')
        books = json.load(file)

        for book in books:
            if book["ISBN"] == request.ISBN:
                bookResponseStatus = inventory_pb2.BookResponseStatus(book=book)
                bookResponseStatus.statusCode = inventory_pb2.SUCCESS
                bookResponseStatus.message = "Book info retrieved successfully!!!"
                return bookResponseStatus

        bookResponseStatus = inventory_pb2.BookResponseStatus()
        bookResponseStatus.statusCode = inventory_pb2.FAILURE
        bookResponseStatus.message = "Failed to retrieve book info!!!"
        return bookResponseStatus

def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventoryService_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
