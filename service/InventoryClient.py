from __future__ import print_function

import logging

import grpc
import inventory_pb2
import inventory_pb2_grpc
import inventoryService_pb2
import inventoryService_pb2_grpc

serverURL = 'localhost:50051'

def run():
    with grpc.insecure_channel(serverURL) as channel:
        stub = inventoryService_pb2_grpc.InventoryServiceStub(channel)
        response = stub.CreateBook(inventory_pb2.Book(ISBN="12348234923",title="title", author="author", genre=inventory_pb2.GENRE_FANTASY,publishingYear=2022))

        if (response.statusCode == inventory_pb2.FAILURE):
            print(response.message)
            return
        
        response = stub.GetBook(inventory_pb2.ISBN(ISBN="12348234923"))

        if (response.statusCode == inventory_pb2.FAILURE):
            print(response.message)
            return
        
        print(response)

if __name__ == '__main__':
    logging.basicConfig()
    run()
