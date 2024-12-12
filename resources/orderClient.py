# from resources.utils.stringFunc import updatePriceStr
# from resources.productCtrl import getProductById
# from resources import inventoryCtrl
# from resources.orderCtrl import createOrder, getOrderById

from utils.globalVar import state
from utils.stringFunc import updatePriceStr
from productCtrl import getProductById
from inventoryCtrl import getInventoryById
from orderCtrl import createOrder, getOrderById, getOrderByStatus


def showOrderInfo(idOrder):
    order = getOrderById(idOrder)
    product = getProductById(order['product'])
    orderInventory = getInventoryById(order['inventory'])
    namePro = product['name']
    print(f'Đơn hàng tạo vào lúc: {order['createdAt']}')
    print('Số lượng:', order['quantity'])
    print('Sản phẩm:', namePro)
    print(f'Giá tiền: {updatePriceStr(orderInventory['price'] * order['quantity'])}')
    print('Loại sản phẩm: ', orderInventory['attribute'])

def showOrdersInfor(orderIds):
    for i in orderIds:
        print(str(i+1) + '.')
        showOrderInfo(i)

def showOrderByStatus(status = 'done'):
    orders = getOrderByStatus(status)
    for order in orders :
        product = getProductById(int(order['product']))
        orderInventory = getInventoryById(order['inventory'])
        namePro = product['name']
        print(f'Đơn hàng tạo vào lúc: {order['createdAt']}')
        print('Số lượng:', order['quantity'])
        print('Sản phẩm:', namePro)
        print(f'Giá tiền: {updatePriceStr(orderInventory['price'] * order['quantity'])}')
        print('Loại sản phẩm: ', orderInventory['attribute'])
        print('Đã thanh toán thành công!')

def showOrdersByStatus(numOrder):
    for num in numOrder:
        print(str(num + 1) + '.')
        showOrderByStatus()

# todo test createOrder function
showOrdersInfor([0])
showOrdersByStatus([0, 1])