from utils.globalVar import Categories, collectionIds
from utils.handleExceptions import elementNotFound
# from resources.utils.globalVar import state, Categories

#state 200
def createCategory(categoryDict):
  try:
    categorynew = categoryDict.copy()
    collectionIds['categoryId'] += 1
    categorynew['id'] = collectionIds['categoryId']
    Categories.append(categorynew)
    return categorynew
  except:
    raise Exception('')

# todo test category
# newCategory = {'name': 'test'}
# createCategory(newCategory)
# print(Categories)

def deleteCategoryById(CategoryId):
  global Categories
  try:
    reqCategory = list(filter(lambda category: category['id'] == CategoryId, Categories))
    Categories.remove(reqCategory[0])

    msg = 'Xóa danh mục thành công!'
    return msg
  except Exception as e: 
    raise Exception(elementNotFound('danh mục'))
  
  #todo test category
# deleteId = 0
# deleteCategoryById(deleteId)
# print(Categories)


def createCategory(categoryDict):
  global Categories, collectionIds
  collectionIds['categoryId'] = collectionIds['categoryId'] + 1
  categoryDict['id'] = collectionIds['categoryId']
  Categories.append(categoryDict)

  msg = 'Tạo danh mục thành công!'
  return {'msg': msg, 'category': categoryDict}


def updateCategoryById(categoryDict):
  try:
    global Categories

    reqCategory = list(filter(lambda category: category['id'] == categoryDict['id'], Categories))
    Indx = Categories.index(reqCategory[0])

    if len(reqCategory) == 0:
      raise Exception(elementNotFound("danh mục"))

    for key in categoryDict: 
      Categories[Indx][key] = categoryDict[key]
    
    msg = 'cập nhật danh mục thành công!'
    return {'msg': msg}
  except:
    raise Exception(elementNotFound("danh mục"))

