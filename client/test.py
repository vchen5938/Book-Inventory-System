import os
import sys
sys.path.append(os.path.dirname(__file__) + '/../service')

import get_book_titles as getBookTitles
import inventory_client as client
import InventoryServer as server
import bookInventoryService as dbService
from unittest.mock import Mock, call
import unittest

SERVER_RUNNING = False

class test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        # arrange
        super(test, self).__init__(*args, **kwargs)
        self.mockResponse = dbService.retrieveListOfBooks()[:3]
        self.expectedTitles = [book.title for book in self.mockResponse]
        self.ISBNs = [book.ISBN for book in self.mockResponse]
        self.inventoryClient = client.InventoryClient()

    def testGetBookTitlesWithMock(self):
        """Tests getting book titles with mock client
        """

        # arrange
        self.inventoryClient.getBook = Mock(side_effect=self.mockResponse)
        calls = [call(ISBN) for ISBN in self.ISBNs]

        # act
        titles = getBookTitles.getTitleLists(self.ISBNs, self.inventoryClient)
        
        # assert
        self.inventoryClient.getBook.assert_has_calls(calls)
        print("Expected Calls:")
        print(calls)
        print("Actual Calls:")
        print(self.inventoryClient.getBook.call_args_list)
        print()
        self.assertEqual(titles, self.expectedTitles)
        print("Expected Titles:")
        print(self.expectedTitles)
        print("Actual Titles:")
        print(titles)

    @unittest.skipIf(not SERVER_RUNNING, "server not running")
    def testGetBookTitlesWithServer(self):
        """Tests getting book titles with real client
        """

        # act
        titles = getBookTitles.getTitleLists(self.ISBNs, self.inventoryClient)

        # assert
        self.assertEqual(titles, self.expectedTitles)
        print("Expected Titles:")
        print(self.expectedTitles)
        print("Actual Titles:")
        print(titles)

if __name__ == '__main__':
    unittest.main()
