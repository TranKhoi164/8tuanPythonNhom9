 pythonEcommerceProject
Bài kiểm tra 8 tuần python nhóm 9

## Services

#### product (state 100 - 199)
- createProduct () - admin
- updateProduct(productId) - admin
- deleteProduct(productId) - admin
- getProducts ()
- getProduct(productId) 

#### inventory:
- createInventory(productId, attributes, quantity, price)
- updateInventory(inventoryDictionary)

categoryDict: {name, value}
#### category (state 200 - 299) ưu tiên
- getCategories()
- createCategory(categoryDict) -admin
- deleteCategory(categoryId) -admin

attribtueDict: {name, value}
#### attribute (state 300 - 399) ưu tiên
- createAttribute(attributeName) -admin
- addAttributeValue(attributeDict) -admin
- deleteAttributeValue(attributeDict) -admin
- getAttributes -admin

#### address (state 400 - ) ưu tiên
- getAddresses()
- createAddress(addressDictionary)
- updateAddress(addressDictionary)
- deleteAddress(addressId)

#### cart (state 500 -)
- getOrdersInCart()
- addToCart(orderId)
- removeFromCart(orderId)
- purchaseAllProducts(orderIdList)
    call purchaseOrders(orderIdList)

orderDict: {productId, inventoryId, addressId, status, quantity}
#### order (state 600 - ) ưu tiên
- createOrder(orderDict)
- getOrders()
- getOrder(orderId)
- updateOrders(orderDict)
- deleteOrder(orderId)
- purchaseOrders(orderIdList)
  

## Tính năng tham gia
### Sản phẩm:
- Tạo sản phẩm: khôi, quang, hiếu
- Xem tóm tắt các sản phẩm: khôi
- Xem chi tiết sản phẩm: khôi, quang, hiếu
- Cập nhật thông tin sản phẩm: khôi, quang, hiếu
- Mua sản phẩm: khôi, quang, khánh
- Thêm sản phẩm vào giỏ hàng: khôi, quang, khánh, hùng
### Danh mục:
- Quản lý danh mục: hiếu
### Địa chỉ:
- Quản lý địa chỉ: quang
### Giỏ hàng:
- Xem các đơn hàng trong giỏ hàng: hùng, khánh
- Thanh toán đơn hàng trong giỏ: hùng, khánh
- Xoá đơn hàng trong giỏ: hùng, khánh
### Đơn hàng:
- Xem các đơn hàng đã thanh toán: khánh

## Service chịu trách nghiệm cụ thể 
- product(productClient, productCtrl): khôi
- attribute(attributeCtrl): hiếu
- category(categoryClient, categoryCtrl): hiếu
- address(addressClient, addressCtrl): quang
- inventory(inventoryCtrl): quang
- order(orderClient, orderCtrl): khánh
- cart(cartClient, cartCtrl): hùng


## Database
<img width="672" alt="Ảnh chụp Màn hình 2024-12-13 lúc 14 07 14" src="https://github.com/user-attachments/assets/a042147d-4794-497d-949e-a73951408eed" />