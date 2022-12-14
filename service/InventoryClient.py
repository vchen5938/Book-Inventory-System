from __future__ import print_function

import logging

import grpc
import book_pb2
import InventoryServer as server
import inventoryService_pb2
import inventoryService_pb2_grpc

class InventoryClient:
    def __init__(self):
        self.serverURL = server.SERVER_URL

    def run(self):
        """Integration test for CreateBook and GetBook
        """

        with grpc.insecure_channel(self.serverURL) as channel:
            stub = inventoryService_pb2_grpc.InventoryServiceStub(channel)
            try:
                response = stub.CreateBook(book_pb2.Book(ISBN="978-3-16-148410-5", title="The Curious Incident of the Dog in the Night-Time", author="Mark Haddon", genre=book_pb2.GENRE_FANTASY, publishingYear=1995))

                print(response)

                response = stub.GetBook(inventoryService_pb2.GetBookRequest(ISBN="978-3-16-148410-5"))
            except grpc.RpcError as e:
                print(e.details())
                return

            print(response)

if __name__ == '__main__':
    logging.basicConfig()
    inventoryClient = InventoryClient()
    inventoryClient.run()
