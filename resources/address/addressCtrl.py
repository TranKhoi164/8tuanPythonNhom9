from utils.globalVar import address

def createAddress(address, ward, district, province):
  newAddress = {
    "address": address,
    "ward": ward,
    "district": district,
    "province": province
  }

  address.append(newAddress)

createAddress("197 minh khai", "vi hoang", "tp namd dinh", "nam dinh")

print(address)
