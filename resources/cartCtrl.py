# from utils.globalVar import Cart, collectionIds
from resources.utils.globalVar import Cart, collectionIds
from resources.utils.handleExceptions import elementNotFound

# todo: khoi them
# add orderId to cart
def addToCart(orderId):
  try:
    cartItem = dict()
    collectionIds['cartId'] += 1
    
    cartItem["id"] = collectionIds['cartId']
    cartItem['order'] = orderId
    Cart.append(cartItem)
  except Exception:
    raise Exception('Thêm vào giỏ hàng thất bại!')
  
def removeFromCart(orderId):
  global Cart
  try:
    reqOrder = list(filter(lambda item: item['order'] == orderId, Cart))
    Cart.remove(reqOrder[0])

    msg = 'Xóa đơn hàng thành công!'
    return msg
  except Exception as e: 
    raise Exception(elementNotFound('sản phẩm')) 

# todo test addTocart
# addToCart(1)
# print(Cart)