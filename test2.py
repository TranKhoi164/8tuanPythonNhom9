# attributes: {'màu': [...], 'size': [...]}
attributes = {'màu': ['đỏ'], 'size': ['l']}
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


getAllProductType(0)
print(tempAttributes)


# getAllProductType(0)
# tempAttributes = [{**i, 'price': '115'} for i in tempAttributes]
# print(tempAttributes)

# print(a)

# def t(li):
#   li.extend([1,2,3])
# l = []
# t(l)
# print(l)
