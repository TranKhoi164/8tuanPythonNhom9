# attributes: {'màu': [...], 'size': [...]}
attributes = {'màu': ['đỏ', 'tím'], 'size': ['l', 'xl', 'm'], 'chất liệu': ['cotton', 'cashmere']}
tempAttributes = []

obj = {}
attKeys = list(attributes.keys())
def getAllProductType(n):
  global obj

  if n > len(attKeys)-1:
    return
  for i in range( 0, len(attributes[attKeys[n]]) ):
    obj = { **obj, attKeys[n]: attributes[attKeys[n]][i] }

    if n < len(attKeys) - 1:
      print(attributes[attKeys[n]][i])
      getAllProductType(n + 1)
    else:
      tempObj = {'attribute': {**obj}}
      tempAttributes.append(tempObj)


def generateInventory(attributes):
  attKeys = attributes.keys()
  getAllProductType(0, attributes)


# getAllProductType(0)
# tempAttributes = [{**i, 'price': '115'} for i in tempAttributes]
# print(tempAttributes)

# print(a)

# def t(li):
#   li.extend([1,2,3])
# l = []
# t(l)
# print(l)
