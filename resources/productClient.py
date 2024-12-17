# from productCtrl import getProducts, createProduct, getProductById, deleteProductById
# from utils.stringFunc import updatePriceStr
# from utils.globalVar import collectionIds, Products, Attributes, state, role

from resources.productCtrl import (
    getProducts,
    createProduct,
    getProductById,
    deleteProductById,
    updateProductById,
)
from resources.utils.stringFunc import updatePriceStr
from resources.utils.globalVar import (
    Inventories,
    role,
)
from resources.inventoryCtrl import (
    createInventory,
    createInventories,
    getInventoryByProductIdAndAttribute,
    updateInventory,
    getInventoriesByProductId,
)
from resources.orderCtrl import createOrder
from resources.cartCtrl import addToCart
from resources.attributeCtrl import updateOrCreateAttribute
import resources.categoryCtrl as categoryCtrl
import resources.addressClient as addressClient
import resources.addressCtrl as addressCtrl


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
    # todo basic info
    print("id:", id)
    print(name)

    reqCategory = categoryCtrl.getCategoryById(category)
    print("Danh mục:", reqCategory["name"])
    # todo attribute
    print("Thuộc tính")
    for i in attributes:
        print(" ", str(i) + ":", attributes[i])
    # todo price
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
    # mau size chatvai

    if n > len(attKeys) - 1:
        return
    for i in range(0, len(attributes[attKeys[n]])):
        obj = {**obj, attKeys[n]: attributes[attKeys[n]][i]}
        if n < len(attKeys) - 1:
            # print(attributes[attKeys[n]][i])
            getAllProductType(n + 1, attributes)
        else:
            tempObj = {"attribute": {**obj}}
            newInventories.append(tempObj)


def enterInventoryInfor(inventories, minPrice, maxPrice):
    inventoryList = []
    newMinPrice = minPrice
    newMaxPrice = maxPrice

    for i in range(0, len(inventories)):
        print(str(i + 1) + ".", inventories[i]["attribute"])
        price = input(
            "Nhập giá (mặc định " + updatePriceStr(inventories[i]["price"]) + "): "
        ).strip()
        if price.isalnum() and int(price) < int(newMinPrice):
            newMinPrice = price
        if price.isalnum() and int(price) > int(newMaxPrice):
            newMaxPrice = price
        quantity = input(
            "Nhập số lượng (mặc định " + str(inventories[i]["quantity"]) + "): "
        ).strip()

        if not price.isalnum():
            price = int(inventories[i]["price"])
        if not quantity.isalnum():
            quantity = int(inventories[i]["quantity"])
        inventoryList.append(
            {
                "attribute": inventories[i]["attribute"],
                "price": price,
                "quantity": quantity,
            }
        )
    return {
        "inventory": inventoryList,
        "minPrice": newMinPrice,
        "maxPrice": newMaxPrice,
    }


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
        newProduct["quantity"] = int(input("Nhập số lượng chung: "))

        # todo: category
        categories = categoryCtrl.getCategories()
        print("Các danh mục hiện có")
        for i in range(len(categories)):
            print(str(i + 1) + ":", categories[i])
        cate = int(input("Nhập id danh mục: "))
        categoryCtrl.getCategoryById(int(cate))
        newProduct["category"] = int(cate)

        # todo: attribute & inventory
        attributeDicts = enterAttributes()

        getAllProductType(0, attributeDicts)

        newInventoriesData = [
            {
                **i,
                "price": int(newProduct["price"]),
                "quantity": int(newProduct["quantity"]),
            }
            for i in newInventories
        ]
        reqInventoriesData = enterInventoryInfor(
            newInventoriesData, newProduct["price"], newProduct["price"]
        )
        newInventoriesData = reqInventoriesData["inventory"]
        newProduct["minPrice"] = int(reqInventoriesData["minPrice"])
        newProduct["maxPrice"] = int(reqInventoriesData["maxPrice"])
        newProduct["attributes"] = attributeDicts
        newInventories.clear()
        obj.clear()
        # todo: details
        detailsArr = enterDetails()
        newProduct["details"] = detailsArr

        # todo: description
        newProduct["description"] = input("Nhập mô tả: ").strip().capitalize()

        # todo: createProduct & inventories
        reqCreateProduct = createProduct(newProduct)
        newInventoriesData = [
            {**i, "product": int(reqCreateProduct["product"]["id"])}
            for i in newInventoriesData
        ]
        createInventories(newInventoriesData)

        if len(newInventoriesData) == 0:
            newInventory = {
                "product": int(reqCreateProduct["product"]["id"]),
                "price": int(newProduct["price"]),
                "quantity": int(newProduct["quantity"]),
            }
            createInventory(newInventory)

        print()
        print(reqCreateProduct["msg"])
        print("--------\n")
    except Exception as e:
        print("Lỗi: ", repr(e))
        print("Tạo sản phẩm thất bại!")
        print("--------\n")


# TODO: state 102
def clientProductDetail(productId):
    try:
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
                clientBuyProduct(productId)
            elif detailOption == "2":
                clientAddProductToCart(productId)
            elif detailOption == "3":
                return
    except Exception as e:
        print("Lỗi: ", repr(e))
        print("Tìm sản phẩm thất bại")


# TODO: state 102_1 update product
def clientUpdateProduct(productId):
    product = getProductById(productId)
    global newInventories
    try:
        global Products, state, newInventories
        updatedProduct = dict()
        print("Chọn trường muốn cập nhật")
        print("1. Tên sản phẩm")
        print("2. Mức giá chung")
        print("3. Số lượng chung")
        print("4. Danh mục")
        print("5. Thuộc tính sản phẩm")
        print("6. Chi tiết sản phẩm")
        print("7. Mô tả sản phẩm")
        option = input("Chọn: ").strip()

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
        elif option == "3":
            updatedProduct["quantity"] = int(input("Nhập số lượng chung: "))
        elif option == "4":
            print("Các danh mục hiện có")
            categories = categoryCtrl.getCategories()
            for i in range(len(categories)):
                print(str(i) + ":", categories[i])
            cate = int(input("Nhập id danh mục: "))
            categoryCtrl.getCategoryById(int(cate))
            updatedProduct["category"] = int(cate)
        elif option == "5":
            # todo: attribute & inventory
            attributeDicts = enterAttributes()

            productInventories = getInventoriesByProductId(product["id"])
            for i in productInventories:
                updateInventory({"id": i["id"], "quantity": 0})

            getAllProductType(0, attributeDicts)
            newInventoriesData = [
                {
                    **i,
                    "price": product["price"],
                    "quantity": product["quantity"],
                }
                for i in newInventories
            ]
            reqInventoriesData = enterInventoryInfor(
                newInventoriesData, product["price"], product["price"]
            )
            newInventoriesData = reqInventoriesData["inventory"]
            updatedProduct["minPrice"] = reqInventoriesData["minPrice"]
            updatedProduct["maxPrice"] = reqInventoriesData["maxPrice"]

            updatedProduct["attributes"] = attributeDicts
            newInventories.clear()
            obj.clear()

            newInventoriesData = [
                {**i, "product": product["id"]} for i in newInventoriesData
            ]
            createInventories(newInventoriesData)

            if len(newInventoriesData) == 0:
                newInventory = {
                    "product": product["id"],
                    "price": product["price"],
                    "quantity": product["quantity"],
                }
                createInventory(newInventory)
        elif option == "6":
            # todo: details
            detailsArr = enterDetails()
            updatedProduct["details"] = detailsArr
        elif option == "7":
            # todo: description
            updatedProduct["description"] = input("Nhập mô tả: ").strip().capitalize()

        # todo: createProduct & inventories
        reqUpdateProduct = updateProductById({"id": product["id"], **updatedProduct})

        print()
        print(reqUpdateProduct["msg"])
        print("--------\n")
    except Exception as e:
        print("Lỗi: ", repr(e))
        print("Cập nhật sản phẩm thất bại!")
        print("--------\n")


# def createNewOrder(attributes):
#     attributeDict = {}
#     for i in attributes:
#         attValue = input("Giá trị thuộc tính " + i + ": ").strip()
#         attributeDict[i] = attValue
#     orderQuantity = int(input("Số lượng: "))

#     print(attributeDict)
#     print("quantity:", orderQuantity)
#     orderDict = {}
#     return orderDict


# todo: 102_2 buy product
def clientBuyProduct(productId):
    product = getProductById(productId)
    try:
        # todo: addrerss
        print("Các địa chỉ hiện có")
        addresses = addressCtrl.getAddresses()
        print(addresses)
        for i in range(0, len(addresses)):
            print(
                str(i + 1) + ". " + 
                "(id " + str(addresses[i]["id"])
                + "): "+str(addresses[i]["address"])
                + ", "
                + str(addresses[i]["ward"])
                + ", "
                + str(addresses[i]["district"])
                + ", "
                + str(addresses[i]["province"]),
            )
        address = int(input("Nhập id địa chỉ: ").strip())

        selectAttDict = {}
        keys = product["attributes"].keys()
        print("Nhập các lựa chọn")
        for i in keys:
            value = input(i + ": ").strip()
            selectAttDict[i] = value
        inventory = getInventoryByProductIdAndAttribute(
            {"attribute": selectAttDict, "productId": product["id"]}
        )

        if inventory["quantity"] == 0:
            raise Exception("Không còn sản phẩm trong kho!")
        quantity = int(
            input(
                "Nhập số lượng muốn mua(còn "
                + str(inventory["quantity"])
                + " sản phẩm): "
            ).strip()
        )

        if quantity > int(inventory["quantity"]) or quantity < 0:
            raise Exception("Số lượng không khả dụng!")

        updateInventory(
            {"id": inventory["id"], "quantity": (int(inventory["quantity"]) - int(quantity))}
        )
        newOrder = {
            "quantity": quantity,
            "product": productId,
            "inventory": inventory["id"],
            "attribute": selectAttDict,
            "address": address,
            "status": "done",
        }
        createOrder(newOrder)
        print("Mua thành công!")
    except Exception as e:
        print("Lỗi: ", repr(e))
        print("Mua sản phẩm thất bại!")


# todo: state 102_3 add product to cart
def clientAddProductToCart(productId):
    product = getProductById(productId)
    try:
        # todo: addrerss
        print("Các địa chỉ hiện có")
        addresses = addressCtrl.getAddresses()
        for i in range(0, len(addresses)):
            print(
                str(i + 1) + ". " + 
                "(id " + str(addresses[i]["id"])
                + "): "+str(addresses[i]["address"])
                + ", "
                + str(addresses[i]["ward"])
                + ", "
                + str(addresses[i]["district"])
                + ", "
                + str(addresses[i]["province"]),
            )
        address = int(input("Nhập id địa chỉ: ").strip())

        # todo: attribute
        selectAttDict = {}
        keys = product["attributes"].keys()
        print("Nhập các lựa chọn")
        for i in keys:
            value = input(str(i) + ": ")
            selectAttDict[i] = value
        inventory = getInventoryByProductIdAndAttribute(
            {"attribute": selectAttDict, "productId": product["id"]}
        )

        if inventory["quantity"] == 0:
            raise Exception("Không còn sản phẩm trong kho!")
        quantity = int(
            input(
                "Nhập số lượng muốn mua(còn "
                + str(inventory["quantity"])
                + " sản phẩm): "
            ).strip()
        )
        newOrder = {
            "quantity": quantity,
            "product": productId,
            "inventory": inventory["id"],
            "attribute": selectAttDict,
            "address": address,
            "status": "pending",
        }
        reqOrder = createOrder(newOrder)
        addToCart(reqOrder["id"])
        print("Thêm vào giỏ hàng thành công!")
    except Exception as e:
        print("Lỗi: ", repr(e))
        print("Thêm vào giỏ hàng thất bại!")


def clientDeleteProduct(productId):
    try:
        print(deleteProductById(productId))
    except Exception as e:
        print(e)


# clientCreateProduct()
# showProducts()
# showProducts()
