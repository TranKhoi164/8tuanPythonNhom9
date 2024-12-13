reqInventory = list(filter(
        lambda i: i['attribute'] == inventoryObj['attribute'] and i['product'] == inventoryObj['productId'], Inventories))
    if len(reqInventory) == 0:
        raise Exception('Không còn sản phẩm trong kho!')
    return reqInventory[len(reqInventory)-1]