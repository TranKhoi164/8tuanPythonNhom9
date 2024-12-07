from .utils.globalVar import Inventories



def them_san_pham(n):
    iD=Inventories[-1]['id']
    dictatribute={'mau':'chua_co','kich thuoc':'chua_co'}
    
    a=['id','product','attribute','quantity','price']
    
    bienmacdinh='chua_co'
    
    b=dict.fromkeys(a,bienmacdinh)
    
    b['id']=iD+1
    
    b['product']=int(input('moi nhap product: '))
    
    print('moi nhap attribute:')
    
    b['attribute']=dictatribute
    
    b["attribute"]['mau']=input('moi nhap mau: ')
    
    b["attribute"]['kich thuoc']=input('moi nhap size: ')
    
    b['quantity']=int(input('moi nhap so luong: '))
    
    b['price']=int(input('moi nhap gia sp: '))
    
    Inventories.append(b)
    print(Inventories)


def xoa_san_pham(n):
    n=int(input('nhap id san pham muon xoa: '))
    for i in Inventories:
        if i['id']==n:
            Inventories.remove(i)
    print(Inventories)

def suasoluong(n):
    print('ban co muon sua so_luong ?')
    print('1. YES')
    print('2. NO')
    traloi=int(input())
    if traloi==1:
        n['quantity']=int(input('moi nhap so luong moi: '))
        print(Inventories)
    elif traloi==2:
        suagiaca(n)
    else:
        unavailableOption()
        suasoluong(n)


def suagiaca(n):
    print('ban co muon sua gia cua san pham ?')
    print('1. YES')
    print('2. NO')
    traloi=int(input())
    if traloi==1:
        n['price']=int(input('moi nhap gia moi: '))
        print(Inventories)
    elif traloi==2:
        suathuoctinh(n)
    else:
        unavailableOption()
        suasoluong(n)


def suathuoctinh(n):
    print('ban co muon sua thuoctinh ?')
    print('1. YES')
    print('2. NO')
    traloi=int(input())
    if traloi==1:
        n["attribute"]["màu "]=input('moi nhap mau moi: ')
        n["attribute"]["kích thước"]=input('moi nhap size moi: ')
        print(Inventories)

        
def update_san_pham():
    n=int(input('nhap id san pham muon sua: '))
    for i in Inventories:
        if i['id']==n:
            suasoluong(i)
            


def unavailableOption():
    print('----Lựa chọn không khả dụng----\n')



#while True:
    #update_san_pham()