from resources.utils.stringFunc import updatePriceStr
from resources.productCtrl import getProductById
from resources.inventoryCtrl import getInventoryById
from resources.orderCtrl import createOrder, getOrderById, getOrdersByStatus
from resources.addressCtrl import getAddressById

# from utils.stringFunc import updatePriceStr
# from productCtrl import getProductById
# from inventoryCtrl import getInventoryById
# from orderCtrl import createOrder, getOrderById, getOrdersByStatus
# from addressCtrl import getAddressById


def showOrderInfo(idOrder):
    order = getOrderById(idOrder)
    product = getProductById(order["product"])
    orderInventory = getInventoryById(order["inventory"])
    address = getAddressById(order["address"])

    namePro = product["name"]
    print("   " + "id:" + str(order["id"]))
    # print(f'   Đơn hàng tạo vào lúc: {order['createdAt']}')
    print('   Đơn hàng tạo vào lúc:', str(order['createdAt']))
    print("   Số lượng:", order["quantity"])
    print("   Sản phẩm:", namePro)
    print(f'   Giá tiền: {updatePriceStr(product['price'] * order['quantity'])}')
    print("   Loại sản phẩm: ", orderInventory["attribute"])
    print(
        "   Địa chỉ: "
        + str(address["address"])
        + ", "
        + str(address["ward"])
        + ", "
        + str(address["district"])
        + ", "
        + str(address["province"])
    )


def clientOrder():
    print('Đơn hàng đã thanh toán:')
    print('--------')
    showOrderStatus()
    select = input('1. Thoát\nChọn: ').strip()
    

def showOrderStatus(status="done"):
    orders = getOrdersByStatus(status)
    for order in orders:
        product = getProductById(order["product"])
        orderInventory = getInventoryById(order["inventory"])
        namePro = product["name"]
        address = getAddressById(order["address"])

        print("   " + "id:" + " " + str(order["id"]))
        # print(f'   Đơn hàng tạo vào lúc: {order['createdAt']}')
        print('   Đơn hàng tạo vào lúc:', str(order['createdAt']))
        print("   Số lượng:", order["quantity"])
        print("   Sản phẩm:", namePro)
        print(f'   Giá tiền: {updatePriceStr(product['price'] * order['quantity'])}')
        print("   Loại sản phẩm: ", orderInventory["attribute"])
        print(
            "   Địa chỉ: "
            + str(address["address"])
            + ", "
            + str(address["ward"])
            + ", "
            + str(address["district"])
            + ", "
            + str(address["province"])
        )
        print('--------')


def showOrdersStatus(numOrder):
    for num in numOrder:
        print("Đơn hàng " + str(num + 1) + ".")
        showOrderStatus()


def showOrdersInfor(orderIds):
    for i in orderIds:
        print("Đơn hàng " + str(i + 1) + ":")
        showOrderInfo(i)


# todo test createOrder function
# showOrdersInfor([0])
# showOrdersByStatus([1])
