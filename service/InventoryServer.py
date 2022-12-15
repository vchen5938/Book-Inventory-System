from concurrent import futures
import logging

import grpc
import inventoryService_pb2
import inventoryService_pb2_grpc
import bookInventoryService

SERVER_URL = "[::]:50051"

class InventoryService(inventoryService_pb2_grpc.InventoryServiceServicer):

    def CreateBook(self, request, context):
        """Creates a book and add it to database.

        Parameters
        ----------
        request : book to be created
        context : server-side context

        Returns
        ------
        Successful response with message
        """

        request = request.book

        # check for invalid ISBN
        if request.ISBN == "":
            context.set_details("Book's ISBN is invalid!!!")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return inventoryService_pb2.CreateBookResponse()
        
        # retrieve list of books from database
        books = bookInventoryService.retrieveListOfBooks()

        # check for duplicate ISBNs
        for book in books:
            if book.ISBN == request.ISBN:
                context.set_details("A book with the same ISBN has been created!!!")
                context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                return inventoryService_pb2.CreateBookResponse()

        # store book to database
        bookInventoryService.storeBooks([request])
        
        context.set_code(grpc.StatusCode.OK)
        return inventoryService_pb2.CreateBookResponse(message="Book created successfully!!!")
    
    def GetBook(self, request, context):
        """Retrieves book details.

        Parameters
        ----------
        request : ISBN of book
        context : server-side context

        Returns
        ------
        Successful response with message and book details
        """

        # check for invalid ISBN
        if request.ISBN == "":
            context.set_details("Book's ISBN is invalid!!!")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return inventoryService_pb2.GetBookResponse()

        # retrieve list of books from database
        books = bookInventoryService.retrieveListOfBooks()

        for book in books:
            if book.ISBN == request.ISBN:
                context.set_code(grpc.StatusCode.OK)
                return inventoryService_pb2.GetBookResponse(message= "Book info retrieved successfully!!!", book=book)

        # failed to find book
        context.set_details("Failed to retrieve book info!!!")
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return inventoryService_pb2.GetBookResponse()

def serve():
    """Starts gRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventoryService_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port(SERVER_URL)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
