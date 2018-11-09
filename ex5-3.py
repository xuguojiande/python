#5.3

def isNum(num):        
        if num == type(1):
            print("True")
        elif num == type(1.0):
            print("True")
        elif num == type(1+1j):
            print("True")
        else:
            print("False")
num = type(eval(input("请输入一个字符串:")))
isNum(num)
