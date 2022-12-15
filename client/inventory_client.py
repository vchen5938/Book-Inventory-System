from __future__ import print_function
import os
import sys
sys.path.append(os.path.dirname(__file__) + '/../service')

import grpc
import inventoryService_pb2 as inventoryService
import inventoryService_pb2_grpc as service
import InventoryServer as server

class InventoryClient:
    def __init__(self):
        channel = grpc.insecure_channel(server.SERVER_URL)
        self.stub = service.InventoryServiceStub(channel)

    def createBook(self, book):
        """Creates desired book

        Parameters
        ----------
        book : book to be created

        Returns
        ------
        Successful response with message
        """

        try:
            response = self.stub.CreateBook(inventoryService.CreateBookRequest(book=book))
        except grpc.RpcError as e:
            print(e.details())
            return

        return response

    def getBook(self, ISBN):
        """Retrieves book info based on a given ISBN

        Parameters
        ----------
        ISBN : ISBN of desired book

        Returns
        ------
        details of desired book
        """

        try:
            response = self.stub.GetBook(inventoryService.GetBookRequest(ISBN=ISBN))
        except grpc.RpcError as e:
            print(e.details())
            return

        return response.book