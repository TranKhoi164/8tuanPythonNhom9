from resources.utils.globalVar import Products, productId
from resources.utils.handleExceptions import elementNotFound

# from utils.globalVar import Products, productId
# from utils.handleExceptions import elementNotFound

def getProducts():
  global Products
  return Products


def getProduct(productId):
  resProduct = list(filter(lambda product: product['id'] == productId, Products))

  if (len(resProduct) > 0):
    return resProduct[0]
  else:
    raise Exception(elementNotFound('sản phẩm'))
  
  
def createProduct(productDict):
  global Products, productId
  productId = productId + 1
  productDict['id'] = productId
  Products.append(productDict)

  msg = 'Tạo sản phẩm thành công!'
  return msg


def updateProduct(productDict):
  try:
    global Products

    reqProduct = list(filter(lambda product: product['id'] == productDict['id'], Products))
    indx = Products.index(reqProduct[0])

    if len(reqProduct) == 0:
      raise Exception(elementNotFound("sản phẩm"))

    for key in productDict: 
      Products[indx][key] = productDict[key]
    
    msg = 'cập nhập sản phẩm thành công!'
    return msg
  except:
    raise Exception(elementNotFound("sản phẩm"))


def deleteProduct(productId):
  global Products
  try:
    reqProduct = list(filter(lambda product: product['id'] == productId, Products))
    Products.remove(reqProduct[0])

    msg = 'Xóa sản phẩm thành công!'
    return msg
  except: 
    return elementNotFound('sản phẩm')
  
    


# try:
#   print(Products)
#   print(deleteProduct(0))
#   print(Products)
# except Exception as e:
#   print(e)
# finally:
#   print('----------\n')