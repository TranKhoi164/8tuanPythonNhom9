# from resources.utils.globalVar import Addresses,collectionIds
# from resources.utils.handleExceptions import elementNotFound

from resources.utils.globalVar import Addresses,collectionIds
from resources.utils.handleExceptions import elementNotFound

        
def getAddresses():
    return Addresses

def getAddressById(addressId):
    for i in range(len(Addresses)):
        if Addresses[i]['id']==addressId:
            return Addresses[i]

def them_addre(n):
    try:
        newadd=n
        collectionIds['addressId']+=1
        newadd['id']=collectionIds['addressId']
        Addresses.append(newadd)
        return "Thêm thành công"
    except Exception as e:
        raise Exception(e)



def sua_addre(addressDict):
    global Addresses

    reqAddress = list(filter(lambda product: product['id'] == addressDict['id'], Addresses))

    if len(reqAddress) == 0:
      raise Exception(elementNotFound("sản phẩm"))
    
    indx = Addresses.index(reqAddress[0])

    for key in addressDict: 
      Addresses[indx][key] = addressDict[key]
    
    msg = 'cập nhật thành công!'
    return {'msg': msg}


def xoa_addre_by_Id(n):
    try:
        for i in range(len(Addresses)):
            if Addresses[i]['id']==n:
                Addresses.pop(i)
                return "Xoá thành công"
    
    except Exception as e:
        raise Exception(e)
    
def get_addre(n):
    for i in range(len(Addresses)):
        if Addresses[i]['id']==n:
            return Addresses[i]
