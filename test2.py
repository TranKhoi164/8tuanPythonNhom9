# from test import state
import utils.globalVar as globalVar

def func1():
  print("1----")
  
  globalVar.state = input('Nhap state: ').strip()
  print('State: ', globalVar.state)

def func2():
  print("2----")  