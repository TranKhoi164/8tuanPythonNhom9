from .utils.globalVar import Inventories ,collectionIds



def them_san_pham(n):
    try:
        newinventory={
            "product": None,
            "attribute": {"màu ": None, "kích thước": None},
            "quantity": None,
            "price": None,
        }

        newinventory=n       
        collectionIds['inventoryId']+=1
        newinventoryID = {'id':collectionIds['inventory']}
        newinventoryID.update(newinventory)
        Inventories.append(newinventoryID)
        
        msd='thành công!'
        return msd
    except:
        mss="LỖI"
        return mss


def showinventory(n):
    n=int(n)
    listinvent=[]
    for inve in Inventories:
        if inve["product"]==n:
            listinvent.append(inve)
    return listinvent


def showIN4inventory(n):
    n=int(n)
    listtrave=[]
    for inve in Inventories:
        if inve["id"]==n:
            listtrave.append(inve)
    return listtrave


def update_san_pham(n):
    for i in range(len(Inventories)):
        if Inventories[i]["id"]==n['id']:
            Inventories[i]['quantity']=n['quantity']
            Inventories[i]['price']=n['price']
            return Inventories
    


