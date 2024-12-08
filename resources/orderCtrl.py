# from utils.globalVar import Orders, collectionIds
from resources.utils.globalVar import Orders, collectionIds
from datetime import datetime

# todo: khoi them
now = datetime.now()
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

# todo test createOrder function
# newOrder = {"product": 0,
#             "inventory": 0,
#             "address": 0,
#             "status": "done",
#             "quantity": 2, }
# createOrder(newOrder)
# print(Orders)
