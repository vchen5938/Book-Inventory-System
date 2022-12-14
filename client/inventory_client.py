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
        self.serverURL = server.SERVER_URL

    def getBook(self, ISBN):
        """Retrieves book info based on a given ISBN

        Parameters
        ----------
        ISBN : ISBN of desired book

        Returns
        ------
        details of desired book
        """

        with grpc.insecure_channel(self.serverURL) as channel:
            stub = service.InventoryServiceStub(channel)
            try:
                response = stub.GetBook(inventoryService.GetBookRequest(ISBN=ISBN))
            except grpc.RpcError as e:
                print(e.details())
                return

            return response.book