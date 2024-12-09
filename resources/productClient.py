# from productCtrl import getProducts, createProduct, getProductById, deleteProductById
# from utils.stringFunc import updatePriceStr
# from utils.globalVar import collectionIds, Products, Attributes, state, role

from resources.productCtrl import (
    getProducts,
    createProduct,
    getProductById,
    deleteProductById,
    updateProductById
)
from resources.utils.stringFunc import updatePriceStr
from resources.utils.globalVar import collectionIds, Products, Attributes, state, role
from resources.inventoryCtrl import createInventory, createInventories
from resources.orderCtrl import createOrder
from resources.cartCtrl import addToCart
from resources.attributeCtrl import updateOrCreateAttribute


def showProductPreview(product):
    id = product["id"]
    name = product["name"]
    price = product["price"]
    minPrice = product["minPrice"]
    maxPrice = product["maxPrice"]

    print("id:", id)
    print(name)
    if minPrice != maxPrice:
        print("Mức giá:", updatePriceStr(minPrice), "-", updatePriceStr(maxPrice))
    else:
        print("Giá:", updatePriceStr(price))


def showProductDetail(product):
    id = product["id"]
    name = product["name"]
    attributes = product["attributes"] or {}
    description = product["description"]
    details = product["details"]
    category = product["category"]
    quantity = product["quantity"]
    price = product["price"]
    minPrice = product["minPrice"]
    maxPrice = product["maxPrice"]

    print("id:", id)
    print(name)

    print("Thuộc tính")
    for i in attributes:
        print(" ", str(i) + ":", attributes[i])

    if minPrice != maxPrice:
        print("Mức giá:", updatePriceStr(minPrice), "-", updatePriceStr(maxPrice))
    else:
        print("Mức giá:", updatePriceStr(price))

    print("Số lượng:", quantity)

    print("Chi tiết sản phẩm")
    for i in details:
        print(" ", i["key"] + ":", i["value"])

    print("Mô tả: ", description)


def showProductsPreview(products):
    print("--------Sản phẩm--------")
    # products = getProducts()
    for product in products:
        showProductPreview(product)
        print("----------------")


# attributes: {'màu': [...], 'size': [...]}
newInventories = []
obj = {}


def getAllProductType(n, attributes):
    global obj
    attKeys = list(attributes.keys())
    if n > len(attKeys) - 1:
        return
    for i in range(0, len(attributes[attKeys[n]])):
        obj = {**obj, attKeys[n]: attributes[attKeys[n]][i]}
        if n < len(attKeys) - 1:
            print(attributes[attKeys[n]][i])
            getAllProductType(n + 1, attributes)
        else:
            tempObj = {"attribute": {**obj}}
            newInventories.append(tempObj)


def enterInventoryInfor(inventories):
    inventoryList = []
    for i in range(0, len(inventories)):
        print(str(i + 1) + ".", inventories[i]["attribute"])
        price = input(
            "Nhập giá (mặc định " + updatePriceStr(inventories[i]["price"]) + "): "
        ).strip()
        quantity = input(
            "Nhập số lượng (mặc định " + str(inventories[i]["quantity"]) + "): "
        ).strip()
        if price.isalnum() == False:
            price = inventories[i]["price"]
        if quantity.isalnum() == False:
            quantity = inventories[i]["quantity"]
        inventoryList.append(
            {**inventories[i]["attribute"], "price": price, "quantity": quantity}
        )
    return inventoryList


def enterAttributes():
    attributeDicts = dict()
    attributesLen = int(input("Số thuộc tính của sản phẩm: "))
    for i in range(0, attributesLen):
        print(str(i + 1) + ".")
        attributeName = input("name: ").strip()
        tempArr = input('values (phân cách bởi dấu ","): ').split(",")

        attributeValues = {s.strip() for s in tempArr}
        attributeValues = list(set(attributeValues))
        # attributeSet = set(attributeValues)
        attributeDicts[attributeName] = attributeValues
        updateOrCreateAttribute({"name": attributeName, "values": attributeValues})
    return attributeDicts


def enterDetails():
    detailsLen = int(input("Số chi tiết của sản phẩm: "))
    detailsArr = []
    for i in range(0, detailsLen):
        newDetail = {}
        print(str(i + 1) + ".")
        newDetail["key"] = input("key: ").strip()
        newDetail["value"] = input("value: ").strip()
        detailsArr.append(newDetail)
    return detailsArr


# TODO: state 101


def clientCreateProduct():
    try:
        global Products, state, newInventories
        newProduct = dict()

        # todo: basic infor
        newProduct["name"] = input("Nhập tên sản phẩm: ").strip().capitalize()
        newProduct["price"] = int(input("Nhập mức giá chung: "))
        newProduct["minPrice"] = newProduct["price"]
        newProduct["maxPrice"] = newProduct["price"]
        newProduct["quantity"] = int(input("Nhập số lượng chung: "))
        newProduct["category"] = int(input("Nhập id danh mục: "))

        # todo: attribute & inventory
        attributeDicts = enterAttributes()

        getAllProductType(0, attributeDicts)
        newInventoriesData = [
            {**i, "price": newProduct["price"], "quantity": newProduct["quantity"]}
            for i in newInventories
        ]
        newInventoriesData = enterInventoryInfor(newInventoriesData)
        newProduct["attributes"] = attributeDicts

        # todo: details
        detailsArr = enterDetails()
        newProduct["details"] = detailsArr

        # todo: description
        newProduct["description"] = input("Nhập mô tả: ").strip().capitalize()

        # todo: createProduct & inventories
        reqCreateProduct = createProduct(newProduct)
        newInventoriesData = [
            {**i, "product": reqCreateProduct["product"]["id"]}
            for i in newInventoriesData
        ]
        createInventories(newInventoriesData)

        if len(newInventoriesData) == 0:
            newInventory = {
                "product": reqCreateProduct["product"]["id"],
                "price": newProduct["price"],
                "quantity": newProduct["quantity"],
            }
            createInventory(newInventory)

        print()
        print(reqCreateProduct["msg"])
        print("--------\n")
    except Exception as e:
        print("Lỗi: ", repr(e))
        print("Tạo sản phẩm thất bại!")
        print("--------\n")


def enterOrderInfor(attributes):
    attributeDict = {}
    for i in attributes:
        attValue = input("Giá trị thuộc tính " + i + ": ").strip()
        attributeDict[i] = attValue
    orderQuantity = int(input("Số lượng: "))

    print(attributeDict)
    print("quantity:", orderQuantity)
    orderDict = {}
    return orderDict


# TODO: state 102
def clientProductDetail(productId):
    product = getProductById(productId)
    showProductDetail(product)

    if role["value"] == "1":
        detailOption = input("1. Sửa sản phẩm\n2. Quay lại\nChọn: ")

        if detailOption == "1":
            clientUpdateProduct(productId)
        elif detailOption == "2":
            return
    elif role["value"] == "2":
        detailOption = input(
            "1. Mua sản phẩm\n2. Thêm sản phẩm vào giỏ hàng\n3. Quay lại\nChọn: "
        )

        if detailOption == "1":
            enterOrderInfor(product["attributes"])
        elif detailOption == "2":
            enterOrderInfor(product["attributes"])
        elif detailOption == "3":
            return


# TODO: state 102_1 update product


def clientUpdateProduct(productId):
    product = getProductById(productId)
    global newInventories
    try:
        global Products, state, newInventories
        updatedProduct = dict()
        print("Chọn trường muốn cập nhật")
        print("1. tên sản phẩm")
        print("2. Mức giá chung")
        print("3. Số lượng chung")
        print("4. Danh mục")
        print("5. Thuộc tính sản phẩm")
        print("6. Chi tiết sản phẩm")
        print("7. Mô tả sản phẩm")
        option = input().strip()

        # newProduct['name'] = input('Nhập tên sản phẩm: ').strip().capitalize()
        # newProduct['price'] = int(input('Nhập mức giá chung: '))
        # newProduct['minPrice'] = newProduct['price']
        # newProduct["maxPrice"] = newProduct['price']
        # newProduct['quantity'] = int(input('Nhập số lượng chung: '))
        # newProduct['category'] = int(input('Nhập id danh mục: '))

        if option == "1":
            updatedProduct["name"] = input("Nhập tên sản phẩm: ").strip().capitalize()
        elif option == "2":
            updatedProduct["price"] = int(input("Nhập mức giá chung: "))
            updatedProduct["minPrice"] = updatedProduct["price"]
            updatedProduct["maxPrice"] = updatedProduct["price"]
        elif option == "3":
            updatedProduct["quantity"] = int(input("Nhập số lượng chung: "))
        elif option == '4':
            updatedProduct["category"] = int(input("Nhập id danh mục: "))
        elif option == '5':
            # todo: attribute & inventory
            attributeDicts = enterAttributes()

            getAllProductType(0, attributeDicts)
            newInventoriesData = [
                {
                    **i,
                    "price": updatedProduct["price"],
                    "quantity": updatedProduct["quantity"],
                }
                for i in newInventories
            ]
            newInventoriesData = enterInventoryInfor(newInventoriesData)
            updatedProduct["attributes"] = attributeDicts
            newInventories = []

            newInventoriesData = [
                {**i, "product": product["product"]["id"]}
                for i in newInventoriesData
            ]
            createInventories(newInventoriesData)
        elif option == '6':
            # todo: details
            detailsArr = enterDetails()
            updatedProduct["details"] = detailsArr
        elif option == '7':
            # todo: description
            updatedProduct["description"] = input("Nhập mô tả: ").strip().capitalize()


        # todo: createProduct & inventories
        reqUpdateProduct = updateProductById({'id': product['id'], **updatedProduct})


        print()
        print(reqUpdateProduct["msg"])
        print("--------\n")
    except Exception as e:
        print("Lỗi: ", repr(e))
        print("Tạo sản phẩm thất bại!")
        print("--------\n")


def clientDeleteProduct(productId):
    try:
        print(deleteProductById(productId))
    except Exception as e:
        print(e)


# clientCreateProduct()
# showProducts()
# showProducts()
