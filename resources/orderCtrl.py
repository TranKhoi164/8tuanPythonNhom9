from resources.utils.globalVar import Orders, collectionIds
from resources.utils.handleExceptions import elementNotFound, unavailableOption
from resources.utils.globalVar import Orders, collectionIds
from datetime import datetime
# from utils.globalVar import Orders, collectionIds
# from utils.handleExceptions import elementNotFound, unavailableOption

# todo: khoi them
now = datetime.now()


def getOrders():
  global Orders
  return Orders

def getOrderById(orderId):
  order = list(filter(lambda order: order['id'] == orderId, Orders))
  return order[0]

# print(getOrderById(0))

def createOrder(orderDict):
  try:
    newOrder = orderDict.copy()
    newOrder["createdAt"] = now.strftime('%d-%m-%Y %H:%M'),
    newOrder["updatedAt"] = now.strftime('%d-%m-%Y %H:%M'),
    collectionIds['orderId'] += 1
    newOrder['id'] = collectionIds['orderId']
    Orders.append(newOrder)
    return newOrder
  except:
    raise Exception('Thêm order thất bại!')
  
def getOrdersByStatus(status):
  order = list(filter(lambda order: order['status'] == status, Orders))
  return order 

# passing a dict to update product
def updateOrderById(orderDict):
  try:
    global Orders

    req = list(filter(lambda order: order['id'] == orderDict['id'], Orders))

    if len(req) == 0:
      raise Exception(elementNotFound("đơn hàng"))
    indx = Orders.index(req[0])

    for key in orderDict: 
      Orders[indx][key] = orderDict[key]
    
    msg = 'cập nhật đơn hàng thành công!'
    return {'msg': msg}
  except:
    raise Exception(elementNotFound("đơn hàng"))

def deleteOrders(orderId):
  try :
    orderDelete = list(filter(lambda orderDel: orderDel['id'] == orderId, Orders))
    Orders.remove(orderDelete[0])
    return 'Xóa thành công!'
  except Exception :
    raise Exception(elementNotFound('đơn hàng'))


# # todo test createOrder function
# newOrder = {"product": 0,
#             "inventory": 0,
#             "address": 0,
#             "status": "done",
#             "quantity": 2 }
# createOrder(newOrder)
# createOrder(newOrder)
# deleteOrders(3)
# print(Orders)

