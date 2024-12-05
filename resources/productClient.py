
# from productCtrl import getProducts
# from utils.stringFunc import updatePriceStr
# from utils.globalVar import Products, productId, state

from resources.productCtrl import getProducts
from resources.utils.stringFunc import updatePriceStr
from resources.utils.globalVar import Products, productId

def showProductDetail(product):
  id = product["id"]
  name = product["name"]
  attributes = product["attributes"] or {}
  description = product["description"]
  details = product["details"]
  category = product["category"]
  price = product["price"]
  minPrice = product["minPrice"]
  maxPrice = product["maxPrice"]
  
  print('id: ', id)
  print(name)

  print('Thuộc tính')
  for i in attributes:
    print(' ', i+':', attributes[i])

  if minPrice != maxPrice:
    print('Mức giá:',updatePriceStr(minPrice),'-', updatePriceStr(maxPrice))
  else:
    print('Mức giá:', updatePriceStr(price))

  print('Chi tiết sản phẩm')
  for i in details:
    print(' ',i['key']+':', i['value'])

  print('Mô tả: ', description)

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


def showProducts():
  print('--------Sản phẩm--------')
  products = getProducts()
  for product in products:
    showProductPreview(product)
    print('----------------')

# state 101
def clientCreateProduct():
  try:
    global Products, state, productId
    newProduct = dict()

    productId += 1
    newProduct["id"] = productId
    newProduct['name'] = input('Nhập tên: ').strip().capitalize()
    newProduct['price'] = int(input('Nhập mức giá chung: ').strip())
    newProduct['minPrice'] = newProduct['price']
    newProduct["maxPrice"] = newProduct['price']
    
    detailsLen = int(input('Số chi tiết của sản phẩm: '))
    detailsArr = []
    
    for i in range(0, detailsLen):
      newDetail = {}
      print(str(i)+'.')
      newDetail['key'] = input('key: ').strip()
      newDetail['value'] = input('value: ').strip()
      detailsArr.append(newDetail)
    newProduct["details"] = detailsArr

    newProduct['description'] = input('Nhập mô tả: ').strip()

    Products.append(newProduct)
    print('Tạo sản phẩm thành công!')
    print('--------\n')
  except Exception as e:
    print('Lỗi: ', repr(e))
    print('Tạo sản phẩm thất bại!')
    print('--------\n')



# clientCreateProduct()
# showProducts()
# showProducts()
