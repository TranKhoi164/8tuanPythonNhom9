# <<<<<<< Updated upstream


#state 200
# =======
from resources.utils.globalVar import Categories, state
from resources.categoryCtrl import createCategory, deleteCategoryById

# state = '0'
#state 200

# >>>>>>> Stashed changes
def clientCategory():
  global state
  print('Các danh mục hiện có')
  for i in range(0, len(Categories)):
      print(str(i+1) + '. ' + 'id: ' + str(Categories[i]['id']) + ', name: ' + Categories[i]['name'])
  print("Quản lí danh mục")
  print("1. Tạo danh mục")
  print("2. Xóa danh mục")
  print("3. Quay lại")
  select = input('Chọn: ').strip()
  if select == '1':
      clientCreateCategory()
  elif select =='2':
      clientDeleteCategory()
  else:
      return  
# <<<<<<< Updated upstream
  
# =======


# TODO: state 201
def clientCreateCategory():
  try:
        global Categories, createCategory, state
        newCategory = dict()

        # todo: basic infor
        newCategory["name"] = input("tên danh mục: ").strip().capitalize()

        reqCreateCategory = createCategory(newCategory)

        print()
        print(reqCreateCategory["msg"])
        print("--------\n")
  except Exception as a:
        print("Lỗi: ", repr(a))
        print("Tạo danh mục thất bại!")
        print("--------\n")


# clientCreateCategory()
# print(Categories)

def clientDeleteCategory():
    global Categories, state
    # # myList = []
    # # clientCreateCategory(myList)
    # for i in myList:
    #     print(i)
    cateId = int(input("Nhập id danh mục bạn muốn xóa:"))
    try:
        print(deleteCategoryById(cateId))
        print('--------\n')
    except Exception as e:
        print(e)



    
# clientDeleteCategory()
# print(Categories)
