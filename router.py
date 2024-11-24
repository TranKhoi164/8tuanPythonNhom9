from resources.utils.globalVar import state
# import test2
import resources.utils.handleExceptions as error
from resources.utils.globalVar import address

# addressId = 0
# addressDatabase = [

# ]

# updateAddress = {
#   "ward": " phuong moi"
# }

# def createAddress(address, ward, district, province):
#   global addressId
#   newAddress = {
#     "id": addressId,
#     "address": address,
#     "ward": ward,
#     "district": district,
#     "province": province
#   } 
#   addressId = addressId + 1

#   addressDatabase.append(newAddress)

# createAddress("197 minh khai", "vi hoang", "tp nam dinh", "nam dinh")
# createAddress("27 minh khai", "vi xuyen", "tp nam dinh", "nam dinh")
# print(addressDatabase)



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

# state 1
def adminClient():
  print('1. Tạo sản phẩm')
  print('2. Xem sản phẩm')
  print('3. Xoá sản phẩm')
  print('4. Quay lại')

  select = input('Chọn: ').strip()

  global state

  if select == '4':
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
  if state == '0':
    getUserRole()
  elif state == '1':
    adminClient()
  elif state == '2':
    customerClient()
  else:
    break
