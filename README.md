# pythonEcommerceProject
Bài kiểm tra 8 tuần python nhóm 9

## Services

#### product (100 - 199)
- createProduct () - admin
- updateProduct(productId) - admin
- deleteProduct(productId) - admin
- getProducts ()
- getProduct(productId)

// inventoryDictionary = {product, attribute, quantity, price}
#### inventory:
- getInventoryOfProduct(productId)
- createInventory(inventoryDictionary)
- updateInventory(inventoryDictionary)

#### category (200 - 299) ưu tiên
- getCategories()
- createCategory(categoryDictionary) -admin
- deleteCategory(categoryId) -admin

#### attribute (300 - 399) ưu tiên
- createAttribute(attributeDictionary) -admin
- addAttributeValue(attributeName, value) -admin
- deleteAttributeValue(attributeName, attributeValue) -admin
- getAttributes 

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
  
// orderDictionary = {productId, inventoryId, addressId, status, quantity}
#### order (600 - ) ưu tiên
- createOrder(orderDictionary)
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

