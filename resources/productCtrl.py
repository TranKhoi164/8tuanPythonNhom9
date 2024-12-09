from resources.utils.globalVar import Products, collectionIds
from resources.utils.handleExceptions import elementNotFound

# from utils.globalVar import Products, productId
# from utils.handleExceptions import elementNotFound

def getProducts():
  global Products
  return Products

# passing productIdList to get a list of product's infor
def getProductsByIds(productIdList):
  resProductList = []

  for productId in productIdList:
    product = list(filter(lambda product: product['id'] == productId, Products))
    resProductList.append(product[0])

  return resProductList

# passing productId to get product's infor
def getProductById(productId):
  resProduct = list(filter(lambda product: product['id'] == productId, Products))

  if (len(resProduct) > 0):
    return resProduct[0]
  else:
    raise Exception(elementNotFound('sản phẩm'))
  
# passing a dict to create new product
def createProduct(productDict):
  global Products, collectionIds
  collectionIds['productId'] = collectionIds['productId'] + 1
  productDict['id'] = collectionIds['productId']
  Products.append(productDict)

  msg = 'Tạo sản phẩm thành công!'
  return {'msg': msg, 'product': productDict}

# passing a dict to update product
def updateProductById(productDict):
  try:
    global Products

    reqProduct = list(filter(lambda product: product['id'] == productDict['id'], Products))
    indx = Products.index(reqProduct[0])

    if len(reqProduct) == 0:
      raise Exception(elementNotFound("sản phẩm"))

    for key in productDict: 
      Products[indx][key] = productDict[key]
    
    msg = 'cập nhật sản phẩm thành công!'
    return {'msg': msg}
  except:
    raise Exception(elementNotFound("sản phẩm"))

# passing a productId to delete
def deleteProductById(productId):
  global Products
  try:
    reqProduct = list(filter(lambda product: product['id'] == productId, Products))
    Products.remove(reqProduct[0])

    msg = 'Xóa sản phẩm thành công!'
    return msg
  except Exception as e: 
    raise Exception(elementNotFound('sản phẩm')) 
  
    


# try:
#   print(getProductById(0))
# except Exception as e:
#   print(e)
# finally:
#   print('----------\n')