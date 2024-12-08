# from utils.globalVar import Cart, collectionIds
from resources.utils.globalVar import Cart, collectionIds

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

# todo test addTocart
# addToCart(1)
# print(Cart)