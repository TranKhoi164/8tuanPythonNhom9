class errorHandler:
    @staticmethod
    def option_not_available():
        print("Tùy chọn không khả dụng. Vui lòng thử lại.\n")
Error = errorHandler()

State = '0'

def OptionCategory(): #Hàm chọn sản phẩm
    global State
    print("1. Áo")
    print("2. Quần")
    print("3. Mỹ phẩm")
    print("4. Giày dép")

    Select = input(" ").strip()
    if Select == '1':
        State = '1'  # Chuyển sang áo
    elif Select == '2':
        State = '2'  # Chuyển sang quần
    elif Select == '3':
        State = '3'  # Chuyển sang mỹ phẩm
    elif Select == '4' :
        State = ' 4' # Chuyển sang giày dép
    else:
        Error.option_not_available()

def Ao():
    global State
    print('Áo')
    print('1. sản phầm 1')
    print('2. sản phẩm 2')
    print('3. sản phẩm 3')
    print('4. Quay lại')
    Select = input('Chọn: ').strip()
    if Select == '4':
        State = '0'
        print('Quay lại màn hình chính.\n')
    else:
        Error.option_not_available()

def Quan():
    global State
    print('Quần')
    print('1. sản phẩm 1')
    print('2. sản phẩm 2')
    print('3. sản phẩm 3')
    print('4. Quay lại')
    Select = input('Chọn: ').strip()
    if Select == '4':
        State = '0'
        print('Quay lại màn hình chính.\n')
    else:
        Error.option_not_available()

def Mypham():
    global State
    print('Mỹ phẩm')
    print('1. sản phẩm 1')
    print('2. sản phẩm 2')
    print('3. sản phẩm 3')
    print('4. Quay lại')
    Select = input('Chọn: ').strip()
    if Select == '4':
        State = '0'
        print('Quay lại màn hình chính.\n')
    else:
      Error.option_not_available()

def Giaydep():
    global State
    print('Mỹ phẩm')
    print('1. sản phẩm 1')
    print('2. sản phẩm 2')
    print('3. sản phẩm 3')
    print('4. Quay lại')
    Select = input('Chọn: ').strip()
    if Select == '4':
        State = '0'
        print('Quay lại màn hình chính.\n')
    else:
      Error.option_not_available()

while True:
    if State == '0':
        OptionCategory()
    elif State == '1':
        Ao()
    elif State == '2':
        Quan()
    elif State == '3':
        Mypham()
    elif State == '4':
        Giaydep()
    elif State == 'exit':
        print("Kết thúc chương trình.")
        break
    else:
        print("Lỗi trạng thái không hợp lệ!")
        break
