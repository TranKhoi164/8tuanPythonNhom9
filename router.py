from resources.utils.globalVar import state, Products, role, Categories
# import test2
import resources.utils.handleExceptions as error
import resources.productCtrl as productCtrl 
import resources.productClient as productClient
import resources.utils.globalVar as globalVar
import resources.categoryClient as categoryClient


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
  print('3. Xoá sản phẩm')
  print('4. Quản lý danh mục')
  print('5. Quản lý thuộc tính')
  print('6. Quay lại')

  select = input('Chọn: ').strip()

  global state
  if select == "1":
    state['value'] = '101'
    print('--------\n')
  elif select == "2":
    state['value'] = '102'
    print('--------\n')
  elif select == "3":
    state['value'] = '103'
    print('--------\n')
  elif select == "4":
    state['value'] = '200'
    print('--------\n')
  elif select == '6':
    state['value'] = '0'
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
      
    
  else:
    break
