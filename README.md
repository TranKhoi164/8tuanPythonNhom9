# pythonEcommerceProject
Bài kiểm tra 8 tuần python nhóm 9

## Services

#### product (100 - 199)
- createProduct () - admin
- updateProduct(productId) - admin
- deleteProduct(productId) - admin
- getProducts ()
- getProduct(productId)

#### inventory:
- createInventory(productId, attributes, quantity, price)
- updateInventory(inventoryDictionary)

#### category (200 - 299) ưu tiên
- getCategories()
- createCategory(categoryName, value) -admin
- deleteCategory(categoryId) -admin

#### attribute (300 - 399) ưu tiên
- createAttribute(attributeName) -admin
- addAttributeValue(attributeName, value) -admin
- deleteAttributeValue(attributeValue) -admin
- getAttributes -admin

#### address (400 - ) ưu tiên
- getAddresses()
- createAddress(...)
- updateAddress(addressDictionary)
- deleteAddress(addressId)

#### cart (500 -)
- getOrdersInCart()
- addToCart(orderId)
- removeFromCart(orderId)
- purchaseAllProducts(orderIdList)
    call purchaseOrders(orderIdList)

#### order (600 - ) ưu tiên
- createOrder(productId, inventoryId, addressId, status, quantity)
- getOrders()
- getOrder(orderId)
- updateOrders(orderDictionary)
- deleteOrder(orderId)
- purchaseOrders(orderIdList)
  

## Phân công
- product, inventory: Khoi, Quang
- category, attribute: hieu
- address, cart: hung
- order: khanh

## Database
![Screenshot 2024-11-24 170936](https://github.com/user-attachments/assets/144ae1d1-4419-4890-81f1-f675bd6e6b13)

