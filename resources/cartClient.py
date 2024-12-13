
# from utils.globalVar import Cart
# import orderClient

from resources.utils.globalVar import Cart
import resources.orderClient as orderClient
import resources.orderCtrl as orderCtrl
import resources.cartCtrl as cartCtrl



def clientPurchaseOrder():
  orderId = int(input('Id đơn hàng muốn thanh toán: ').strip())

  orderCtrl.updateOrderById({'id': orderId, 'status': 'done'})
  cartCtrl.removeFromCart(orderId)

  print('Thanh toán đơn hàng thành công!')
  print('--------\n')

def clientRemoveOrderFromCart():
  orderId = int(input('Id đơn hàng muốn xóa: ').strip())

  orderCtrl.updateOrderById({'id': orderId, 'status': 'done'})
  cartCtrl.removeFromCart(orderId)
  orderCtrl.deleteOrders(orderId)
  print('Xóa đơn hàng thành công!')
  print('--------\n')

def clientPurchaseAllOrders():
  for i in Cart:
    orderCtrl.updateOrderById({'id': i['id'], 'status': 'done'})
    cartCtrl.removeFromCart(i['id'])
    orderCtrl.deleteOrders(i['id'])
  print("Thanh toán toàn bộ thành công!")
  print('--------\n')

def showCartItems():
  for i in Cart:
    orderClient.showOrderInfo(i['id'])
    print('--------')

def clientCart():
  print('Đơn hàng hiện có')
  print('--------')
  showCartItems()
  print('1. Thanh toán đơn hàng')
  print('2. Xóa đơn hàng khỏi giỏ hàng')
  print('3. Thanh toán tất cả đơn hàng')
  print('4. Thoát')
  select = input('Chọn: ').strip()

  if select == '1':
    clientPurchaseOrder()
  elif select == '2':
    clientRemoveOrderFromCart()
  elif select == '3':
    clientPurchaseAllOrders()
  else:
    return




