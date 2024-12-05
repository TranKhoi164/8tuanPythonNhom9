from resources.utils.globalVar import state
# import test2
import resources.utils.globalVar 
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
    state = '1'
  elif role == "2":
    state = '2'
  else:
    state = '0'
    error.unavailableOption()
  print('--------\n')

# state 1
def adminClient():
  productClient.showProducts()
  print('1. Tạo sản phẩm')
  print('2. Xem sản phẩm')
  print('3. Xoá sản phẩm')
  print('4. Quay lại')

  select = input('Chọn: ').strip()

  global state
  if select == "1":
    state = '101'
    print('--------\n')
  elif select == '4':
    state = '0'
    print('--------\n')
  else:
    state = '1'
    error.unavailableOption()

# state 2
def customerClient():
  print('1. Tạo sản phẩm')
  print('2. Xem sản phẩm')
  print('3. Xoá sản phẩm')
  print('4. Quay lại')
  select = input('')



while True:
  print('state:', state)
  if state == '0':
    getUserRole()
  elif state == '1':
    adminClient()
  elif state == '2':
    customerClient()
  elif state == '101':
    productClient.clientCreateProduct()
    state = '1'
  else:
    break
