from datetime import datetime

state = "0"

categoryId = 0
categories = [{"id": 0, "name": "váy"}]

attributeId = 1
attributes = [
    {"id": 0, "name": "màu", "values": ["đỏ", "vàng"]},
    {"id": 1, "name": "kích thước", "values": ["l", "xl"]},
]

addressId = 0
addresses = [
    {
        "id": 0,
        "address": "197 minh khai",
        "ward": "phường vị hoàng",
        "district": "tp nam định",
        "province": "tỉnh nam định",
    }
]


productId = 0
products = [
    {
        "id": 0,
        "category": "0",
        "name": "Váy nữ viền lá sen thanh lịch",
        "description": "Váy cho bạn nữ để đi chơi & mặc ở nhà",
        "attributes": {
            "màu ": ["đỏ", "vàng"],
            "kích thước": ["l", "xl"],
        },
        "detail": [
            {"key": "phong cách", "value": "thanh lịch"},
            {"key": "vòng eo", "value": "cao"},
            {"key": "sợi vải", "value": "căng nhẹ"},
        ],
        "price": 364000,
        "inventories": [1, 2, 3, 4],
        "maxPrice": 364000,
        "minPrice": 364000,
    }
]

inventories = [
    {
        "id": 0,
        "product": 0,
        "attribute": {"màu ": "đỏ", "kích thước": "l"},
        "quantity": 113,
        "price": 364000,
    },
    {
        "id": 1,
        "product": 0,
        "attribute": {"màu ": "đỏ", "kích thước": "xl"},
        "quantity": 115,
        "price": 364000,
    },
    {
        "id": 2,
        "product": 0,
        "attribute": {"màu ": "vàng", "kích thước": "l"},
        "quantity": 115,
        "price": 364000,
    },
    {
        "id": 3,
        "product": 0,
        "attribute": {"màu ": "vàng", "kích thước": "xl"},
        "quantity": 115,
        "price": 364000,
    },
]

now = datetime.now()
orderId = 0
orders = [
    {
        "id": 0,
        "product": 0,
        "inventory": 0,
        "address": 0,
        "status": "done",
        "quantity": 2,
        "createdAt": now.strftime('%d-%m-%Y %H:%M'),
        "updatedAt": now.strftime('%d-%m-%Y %H:%M'),
    }
]