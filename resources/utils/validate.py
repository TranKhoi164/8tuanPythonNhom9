from utils.globalVar import Categories
from utils.handleExceptions import elementNotFound

def validateProduct(productDict):
  category = list(filter(lambda category: category["id"] == productDict['category'], Categories))
  if len(productDict["name"]) == 0:
    raise Exception("Cần nhập tên sản phẩm!")
  elif len(productDict["description"]) == 0:
    raise Exception("Cần nhập mô tả sản phẩm!")
  elif len(category) == 0:
    raise Exception(elementNotFound('category'))
  