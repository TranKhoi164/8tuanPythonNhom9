import resources.utils.globalVar as globalVar
import resources.utils.handleExceptions as error

def getCategories():
  return globalVar.Categories

def getCategoryById(cateId):
  reqCategory = list(filter(
        lambda i: i['id'] == cateId, globalVar.Categories))
  if len(reqCategory) == 0:
        raise Exception(error.elementNotFound('danh mục'))
  return reqCategory[len(reqCategory)-1]