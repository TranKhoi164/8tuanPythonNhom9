# from utils.globalVar import Attributes, collectionIds

from resources.utils.globalVar import Attributes, collectionIds

# todo: khoi them
# update attribute by 'name', or create new attribute if element doesn't exist
def updateOrCreateAttribute(attributeDict):
    attributeDict['values'] = list(set(attributeDict['values']))
    try:
        reqAttribute = list(filter(
            lambda attribute: attribute['name'] == attributeDict['name'], Attributes))

        if len(reqAttribute) == 0:
            collectionIds['attributeId'] += 1
            newA = {'id': collectionIds['attributeId'], **attributeDict}
            Attributes.append(newA)
            return 'Tạo mới thành công!'

        indx = Attributes.index(reqAttribute[0])
        Attributes[indx]['values'].extend(attributeDict['values'].copy())
        Attributes[indx]['values'] = list(set(Attributes[indx]['values']))

        msg = 'cập nhật thành công!'
        return msg
    except Exception as e:
        raise Exception('Thêm hoặc sửa attribute thất bại!')

# todo: test function 'updateOrCreateAttribute'
# test = {'name': 'màu', 'values': {'xanh', 'trắng', 'đen'}}
# updateOrCreateAttribute(test)
# print(Attributes)
