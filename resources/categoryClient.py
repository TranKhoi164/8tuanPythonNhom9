# <<<<<<< Updated upstream


#state 200
# =======
from utils.globalVar import Categories, state
from categoryCtrl import createCategory, deleteCategoryById

state = '0'
#state 200

# >>>>>>> Stashed changes
def clientCategory():
  global state
  print("Quản lí danh mục")
  print("1. Tạo danh mục")
  print("2. Xóa danh mục")
  print("3. Quay lại")
  select = input()
  if select == '4':
    return
# <<<<<<< Updated upstream
  
# =======
  elif select == '1':
      state = '1'
  elif select == '2':
      state ='2'


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
    except Exception as e:
        print(e)


    
# clientDeleteCategory()
# print(Categories)

# while True:
#     if state == '0':
#         clientCategory()
#     elif state =='1':
#         clientCreateCategory()
#     elif state == '2':
#         clientDeleteCategory()
#     elif state  == 'exit':
#         print("Kết thúc chương trình.")
#         break
#     else:
#         print("Lỗi trạng thái không hợp lệ!")
#         break
# >>>>>>> Stashed changes
