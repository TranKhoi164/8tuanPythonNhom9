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
    if order['status'] == 'done' :
        product = getProductById(order['product'])
        orderInventory = getInventoryById(order['inventory'])
        namePro = product['name']
        print(f'Đơn hàng tạo vào lúc: {order['createdAt']}')
        print('Số lượng:', order['quantity'])
        print('Sản phẩm:', namePro)
        print(f'Giá tiền: {updatePriceStr(orderInventory['price'] * order['quantity'])}')
        print('Loại sản phẩm: ', orderInventory['attribute'])
        print('Thanh toán thành công!')

def showOrdersInfor(orderIds):
    for i in orderIds:
        print(str(i+1) + '.')
        showOrderInfo(i)


# todo test createOrder function
showOrdersInfor([0])