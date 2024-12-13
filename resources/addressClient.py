from resources.utils.globalVar import Addresses,collectionIds
from resources.utils.handleExceptions import elementNotFound
import resources.addressCtrl as addressCtrl

# def show_address(n):
#     for i in range(len(Addresses)):
#         if Addresses[i]['id']==n:
#             print("dia chi cua ban: "+ Addresses[i]["address"] +','
#                   +Addresses[i]["ward"]+','+Addresses[i]["district"]
#                   +','+Addresses[i]["province"]+'.')

def show_addresses():
    tt=1
    for i in Addresses:
        print(str(tt)+'.')
        print('id: ', str(i['id']))
        print('Địa chỉ: ',str(i['address']))
        print('Phường: ',str(i['ward']))
        print('Thành_phố/quận/huyện: ',str(i['district']))
        print('Tỉnh: ',str(i['province']))
        tt+=1
        print('--------')

# state 400
def clientAddress():
    print('Địa chỉ hiện có')
    print('--------')
    show_addresses()
    print("1. Thêm địa chỉ")
    print("2. Sửa địa chỉ")
    select=int(input('Chọn: '))
    if select==1:
        clientCreateAddress()
    elif select==2:
        clientUpdateAddress()
    else:
        print("Lựa chọn không khả dụng,vui lòng thực hiện lại!")
        clientAddress()

def enterAddress():
    newadd={}
    
    newadd["address"]=input('Địa chỉ: ')
    newadd['ward']=input('Phường: ')
    newadd["district"]=input('Thành phố/quận/huyện: ')
    newadd["province"]=input('Tỉnh thành: ')

    return newadd

# TODO: state 401
def clientCreateAddress():
    print('Nhập thông tin địa chỉ')
    newadd=enterAddress()
    print(addressCtrl.them_addre(newadd))



# TODO: state 402
def clientUpdateAddress():
    try:
        # addresses = addressCtrl.getAddresses()
        # print('Các địa chỉ hiện có:')
        # for i in range(0, len(addresses)):
        #     print(str(i)+'.', addresses[i])
        addressId = int(input('Nhập id địa chỉ muốn sửa: '))
        print('Sửa thông tin địa chỉ')
        updateAddressInfor = enterAddress()

        print(addressCtrl.sua_addre({'id': int(addressId), **updateAddressInfor}))
    except Exception as e:
        print('Lỗi: ', repr(e))
        print('Sửa địa chỉ thất bại!')
        print('--------')
    

# print(show_addresses())