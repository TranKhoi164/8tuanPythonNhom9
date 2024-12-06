
# from productCtrl import getProducts
# from utils.stringFunc import updatePriceStr
# from utils.globalVar import Products, productId, state

from resources.productCtrl import getProducts, createProduct, getProductById, deleteProductById
from resources.utils.stringFunc import updatePriceStr
from resources.utils.globalVar import collectionIds, Products, Attributes, state, role


def showProductPreview(product):
  id = product["id"]
  name = product["name"]
  price = product["price"]
  minPrice = product["minPrice"]
  maxPrice = product["maxPrice"]

  print('id:', id)
  print(name)
  if minPrice != maxPrice:
    print('Mức giá:',updatePriceStr(minPrice),'-', updatePriceStr(maxPrice))
  else:
    print('Giá:', updatePriceStr(price))


def showProductDetail(product):
  id = product["id"]
  name = product["name"]
  attributes = product["attributes"] or {}
  description = product["description"]
  details = product["details"]
  category = product["category"]
  quantity = product['quantity']
  price = product["price"]
  minPrice = product["minPrice"]
  maxPrice = product["maxPrice"]
  
  print('id:', id)
  print(name)

  print('Thuộc tính')
  for i in attributes:
    print(' ', str(i)+':', attributes[i])

  if minPrice != maxPrice:
    print('Mức giá:',updatePriceStr(minPrice),'-', updatePriceStr(maxPrice))
  else:
    print('Mức giá:', updatePriceStr(price))
  
  print('Số lượng:', quantity)

  print('Chi tiết sản phẩm')
  for i in details:
    print(' ',i['key']+':', i['value'])

  print('Mô tả: ', description)



def showProductsPreview(products):
  print('--------Sản phẩm--------')
  # products = getProducts()
  for product in products:
    showProductPreview(product)
    print('----------------')


# state 101
def clientCreateProduct():
  try:
    global Products, state
    newProduct = dict()
    
    newProduct['name'] = input('Nhập tên sản phẩm: ').strip().capitalize()
    newProduct['price'] = int(input('Nhập mức giá chung: '))
    newProduct['minPrice'] = newProduct['price']
    newProduct["maxPrice"] = newProduct['price']
    newProduct['quantity'] = int(input('Nhập số lượng chung: '))
    newProduct['category'] = int(input('Nhập id danh mục: '))

    attributesLen = int(input('Số thuộc tính của sản phẩm: '))
    attributesDict = {}
    for i in range(0, attributesLen):
      print(str(i+1)+'.')
      attributeName = input('name: ').strip()
      tempArr = input('values (phân cách bởi dấu ","): ').split(',')
      attributeValues = {s.strip() for s in tempArr}
      attributesDict[attributeName] = attributeValues
    newProduct['attributes'] = attributesDict

    detailsLen = int(input('Số chi tiết của sản phẩm: '))
    detailsArr = []
    for i in range(0, detailsLen):
      newDetail = {}
      print(str(i+1)+'.')
      newDetail['key'] = input('key: ').strip()
      newDetail['value'] = input('value: ').strip()
      detailsArr.append(newDetail)
    newProduct["details"] = detailsArr

    newProduct['description'] = input('Nhập mô tả: ').strip().capitalize()

    print(newProduct)
    print()
    print(createProduct(newProduct))
    # print('Tạo sản phẩm thành công!')
    print('--------\n')
  except Exception as e:
    print('Lỗi: ', repr(e))
    print('Tạo sản phẩm thất bại!')
    print('--------\n')
    state['value'] = '1'


def enterOrderInfor(attributes):
  attributeDict = {}
  for i in attributes:
    attValue = input('Giá trị thuộc tính ' + i + ': ').strip()
    attributeDict[i] = attValue
  orderQuantity = int(input('Số lượng: '))

  print(attributeDict)
  print('quantity:', orderQuantity)
  orderDict = {}
  return orderDict



# state 102
def clientProductDetail(productId):
  product = getProductById(productId)
  showProductDetail(product)
  
  if role['value'] == '1':
    detailOption = input('1. Sửa sản phẩm\n2. Quay lại\nChọn: ')

    if detailOption == '1':
      enterOrderInfor(product['attributes'])
    elif detailOption == "2":
      enterOrderInfor(product['attributes'])
    elif detailOption == "3":
      return
  elif role['value'] == '2':
    detailOption = input('1. Mua sản phẩm\n2. Thêm sản phẩm vào giỏ hàng\n3. Quay lại\nChọn: ')

    if detailOption == '1':
      enterOrderInfor(product['attributes'])
    elif detailOption == "2":
      enterOrderInfor(product['attributes'])
    elif detailOption == "3":
      return
    

def clientDeleteProduct(productId):
  try:
    print(deleteProductById(productId))
  except Exception as e:
    print(e)
  




# clientCreateProduct()
# showProducts()
# showProducts()
