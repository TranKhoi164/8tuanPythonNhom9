from resources.utils.globalVar import state, Products
# import test2
import resources.utils.handleExceptions as error
import resources.productCtrl as productCtrl 
import resources.productClient as productClient


# state 0
def getUserRole():
  print('1. admin')
  print('2. customer')
  role = input('Bạn là: ').strip()
  global state
  if role == '1':
    state['value'] = '1'
  elif role == "2":
    state['value'] = '2'
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
  elif select == '4':
    state['value'] = '0'
    print('--------\n')
  else:
    state['value'] = '1'
    error.unavailableOption()

# state 2
def customerClient():
  productClient.showProductsPreview(Products)
  print('1. Tạo sản phẩm')
  print('2. Xem sản phẩm')
  print('3. Xoá sản phẩm')
  print('4. Quay lại')

  select = input('Chọn: ').strip()

  global state
  if select == "1":
    state['value'] = '101'
    print('--------\n')
  elif select == '4':
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
    productClient.clientCreateProduct()
    state['value'] = '1'
  else:
    break
