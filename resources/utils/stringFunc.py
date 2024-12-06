# chuyển dạng price vd 30000 => 30.000đ
def updatePriceStr(price):
  price = str(price)
  i = len(price) - 3
  res = price

  while i > 0:
    res = res[:i] + '.' + res[i:]
    i -= 3 
  return res + 'đ'

