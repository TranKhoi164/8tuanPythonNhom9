# <<<<<<< Updated upstream
# from utils.globalVar import Inventories ,collectionIds
# from utils.handleExceptions import elementNotFound

# from utils.globalVar import Inventories, collectionIds
from resources.utils.globalVar import Inventories, collectionIds
from resources.utils.handleExceptions import elementNotFound


# =======


# todo: khoi them

def createInventory(inventoryDict):
    try:
        collectionIds['inventoryId'] += 1
        newI = inventoryDict.copy()
        newI['id'] = collectionIds['inventoryId']
        Inventories.append(newI)
        return newI
    except Exception as e:
        raise Exception(e)
# todo: test function createInventory
# test = {"product": 0,
#         "attribute": {"màu ": "đỏ", "kích thước": "l"},
#         "quantity": 113,
#         "price": 364000,}
# createInventory(test)
# print(Inventories)


def createInventories(inventories):
    try:
        for i in inventories:
            createInventory(i)
    except Exception as e:
        raise Exception(e)
# todo: test function createInventories
# test = [{"product": 0,
#         "attribute": {"màu ": "đỏ", "kích thước": "l"},
#         "quantity": 113,
#         "price": 364000,},
#         {"product": 0,
#         "attribute": {"màu ": "xanh", "kích thước": "xm"},
#         "quantity": 113,
#         "price": 364000,}]
# createInventories(test)
# print(Inventories)


def them_san_pham(n):
    try:
        newinventory = {
            "product": None,
            "attribute": {"màu ": None, "kích thước": None},
            "quantity": None,
            "price": None,
        }

        newinventory = n
        collectionIds['inventoryId'] += 1
        newinventoryID = {'id': collectionIds['inventory']}
        newinventoryID.update(newinventory)
        Inventories.append(newinventoryID)

        msd = 'thành công!'
        return msd
    except:
        mss = "LỖI"
        return mss


def showinventory(n):
    n = int(n)
    listinvent = []
    for inve in Inventories:
        if inve["product"] == n:
            listinvent.append(inve)
    return listinvent


def showIN4inventory(n):
    n = int(n)
    listtrave = []
    for inve in Inventories:
        if inve["id"] == n:
            listtrave.append(inve)
    return listtrave


def updateInventory(inventoryDict):
    reqInventory = list(filter(
        lambda i: i['id'] == inventoryDict['id'], Inventories))
    if len(reqInventory) == 0:
        raise Exception(elementNotFound('inventory'))
    inventoryIndex = Inventories.index(reqInventory[0])
    Inventories[inventoryIndex] = inventoryDict.copy()
    msg = 'Cập nhật thành công!'
    return {'msg': msg, 'inventory': inventoryDict}
# TODO: test updateInventory
# test = {"id": 0,
#         "product": 0,
#         "attribute": {"màu ": "xanh", "kích thước": "xl"},
#         "quantity": 200,
#         "price": 2000000,}
# t = updateInventory(test)
# print(t['inventory'])


# <<<<<<< Updated upstream

# =======
# while True:
    # update_san_pham()
# >>>>>>> Stashed changes
