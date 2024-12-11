

#state 200
def clientCategory():
  global state
  print("Quản lí danh mục")
  print("1. Tạo danh mục")
  print("2. Xóa danh mục")
  print("3. Quay lại")
  select = input()
  if select == '4':
    return
  
