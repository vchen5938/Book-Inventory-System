import inventory_client as client

def getTitleLists(ISBNs, inventoryClient):
    """Retrieves list of book titles given a list of ISBNs

    Parameters
    ----------
    ISBNs : ISBNs of desired books
    inventoryClient: Client API object

    Returns
    ------
    list of desired book titles
    """

    titles = []
    for ISBN in ISBNs:
        book = inventoryClient.getBook(ISBN)
        if book:
            titles.append(book.title)
    
    return titles

if __name__ == '__main__':
    # create real client object
    inventoryClient = client.InventoryClient()
    # call the defined function with two ISBNs
    ISBNs = ["978-3-16-148410-3", "978-3-16-148410-2"]
    titles = getTitleLists(ISBNs, inventoryClient)
    # print returned titles
    print(titles)