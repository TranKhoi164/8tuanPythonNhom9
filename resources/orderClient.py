from resources.utils.stringFunc import updatePriceStr
from resources.productCtrl import getProductById
from resources import inventoryCtrl, getInventoryById
from resources.orderCtrl import createOrder, getOrderById

# from utils.stringFunc import updatePriceStr
# from productCtrl import getProductById
# from inventoryCtrl import getInventoryById
# from orderCtrl import createOrder, getOrderById


def showOrderInfo(idOrder):
    order = getOrderById(idOrder)
    product = getProductById(order['product'])
    orderInventory = getInventoryById(order['inventory'])
    namePro = product['name']
    print(f'Đơn hàng tạo vào lúc: {order['createdAt']}')
    print('Số lượng:', order['quantity'])
    print('Sản phẩm:', namePro)
    print(f'Giá tiền: {updatePriceStr(product['price'] * order['quantity'])}')
    print('Loại sản phẩm: ', orderInventory['attribute'])
    
    if order['status'] == 'done' :
        print('Trạng thái: Đã thanh toán!')
    else :
        print('Trạng thái: Chưa thanh toán!')

def showOrdersInfor(orderIds):
    for i in orderIds:
        print(str(i+1) + '.')
        showOrderInfo(i)


# todo test createOrder function
# showOrdersInfor([0])