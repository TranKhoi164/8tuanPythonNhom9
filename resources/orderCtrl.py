from datetime import datetime
import random
import time

def errorSelect():
    print('-----Lựa chọn không khả dụng-----\n') 

def overload():
    print('-----Mặt hàng hiện tạm không còn trong kho-----\n') 

def count():
    num = 10 
    while num > 0:
        print('.', end = '') 
        time.sleep(0.2) 
        num -= 1
    print()  

now = datetime.now()

def check_pay(): # Kiểm tra đơn hàng được thanh toán chưa
    print('Bạn muốn thanh toán bằng phương thức nào:') 
    print('1. Thanh toán bằng tiền mặt') 
    print('2. Thanh toán qua tài khoản ngân hàng') 

    id = input()
    if id == '1' :
        print('Vui lòng thanh toán cho người giao hàng!')
    elif id == '2' :
        print('Vui lòng quý khách thanh toán qua STK:') 
        print('-------0123456789 (Vietcombank)-------')
        print('Giao dịch thành công!')
        print(f"{'Đơn hàng được thanh toán vào thời điểm: '}{now.strftime('%d-%m-%Y %H:%M')}")
    else :
        errorSelect() 
        check_pay()

class Products:
    def __init__(self, name_product, size, price, inventory):
        self.name_product = str(name_product)
        self.size = str(size) 
        self.price = int(price)
        self.inventory = int(inventory)

class Orders:
    def __init__(self):
        self.order = [] 
    
    def check_order(self, product, order_in):
        if product.inventory < order_in :
            overload() 
        else :
            self.order.append(
                {
                    'prod': product, 
                    'quantity': order_in
                }
            )
            product.inventory -= order_in

    def display_order(self):
        for ode in self.order:
            product = ode['prod'] 
            quantity = ode['quantity'] 
            total_cost = product.price * quantity
            idproduct = ''
            for i in product.name_product.split():
                idproduct += i[0] 
            idproduct = idproduct.upper()
            print(f"Đơn hàng {product.name_product} của quý khách với mã đơn là: {idproduct}") 
            print(f"Tổng giá tiền: {product.price} * {quantity} = {total_cost}")
            count() 
            check_pay() 
    
def update_order():
    print('Quý khách có mua thêm mặt hàng nào không?') 
    print('1. Có') 
    print('2. Không') 
    count()
    choice = int(input())
    if choice == 2 :
        print('Cảm ơn quý khách đã mua hàng!') 
        print('--------Hẹn gặp lại!--------') 
    elif choice == 1 :
        new_order = Orders()
        new_order.order.clear()
        p2 = Products('Quan dai ong rong', '2xl', 450000, 30) 
        new_order.check_order(p2, 4)
        new_order.display_order()

p1 = Products('Vay ngan', 'l', 300000, 10) 
ords = Orders()
ords.check_order(p1, 4) 
ords.display_order() 
update_order()
