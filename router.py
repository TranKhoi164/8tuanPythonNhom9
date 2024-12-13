from resources.utils.globalVar import state, Products, role, Categories
# import test2
import resources.utils.handleExceptions as error
import resources.productCtrl as productCtrl 
import resources.productClient as productClient
import resources.utils.globalVar as globalVar
import resources.categoryClient as categoryClient
import resources.cartClient as cartClient
import resources.orderClient as orderClient
import resources.addressClient as addressClient



# state 0
def getUserRole():
  print('1. admin')
  print('2. customer')
  roleOption = input('Bạn là: ').strip()

  if roleOption == '1':
    state['value'] = '1'
    role['value'] = '1'
  elif roleOption == "2":
    state['value'] = '2'
    role['value'] = '2'
  else:
    state['value'] = '0'
    error.unavailableOption()
  print('--------\n')

# state 1
def adminClient():
  productClient.showProductsPreview(Products)
  print('1. Tạo sản phẩm')
  print('2. Xem sản phẩm')
  print('3. Quản lý danh mục')
  print('4. Quay lại')

  select = input('Chọn: ').strip()

  global state
  if select == "1":
    state['value'] = '101'
    print('--------\n')
  elif select == "2":
    state['value'] = '102'
    print('--------\n')
  elif select == "3":
    state['value'] = '200'
    print('--------\n')
  else:
    state['value'] = '1'
    error.unavailableOption()

# state 2
def customerClient():
  productClient.showProductsPreview(Products)
  print('1. Xem sản phẩm')
  print('2. Giỏ hàng')
  print('3. Đơn hàng của bạn')
  print('4. Thông tin địa chỉ')
  print('5. Quay lại')

  select = input('Chọn: ').strip()

  global state
  if select == "1":
    state['value'] = '102'
    print('--------\n')
  elif select == '2':
    state['value'] = '500'
  elif select == '3':
    state['value'] = '600'
  elif select == '4':
    state['value'] = '400'
  elif select == '5':
    state['value'] = '0'
    print('--------\n')
  else:
    state['value'] = '1'
    error.unavailableOption()


while True:
  if state['value'] == '0':
    getUserRole() 
  elif state['value'] == '1':
    adminClient()
  elif state['value'] == '2':
    customerClient()
  elif state['value'] == '101':
    # tao san pham
    productClient.clientCreateProduct()
    state['value'] = '1'
  elif state['value'] == '102':
    # xem chi tiet san pham
    productId = int(input("Nhập id sản phẩm: "))
    productClient.clientProductDetail(productId)
    
    if role['value'] == '1': 
      state['value'] = '1'
    elif role["value"] == "2": 
      state["value"] = "2"

  elif state['value'] == '103':
    productId = int(input("Nhập id sản phẩm: "))
    productClient.clientDeleteProduct(productId)
    state['value'] = '1'

  elif state['value'] == '200':
    categoryClient.clientCategory()
    state['value'] = '1'
  elif state['value'] == '400':
    addressClient.clientAddress()
    state['value'] = '2'
  elif state['value'] == '500':
    cartClient.clientCart()
    state['value'] = '2'
  elif state['value'] == '600':
    orderClient.clientOrder()
    state['value'] = '2'
  else:
    state['value'] = '0'
