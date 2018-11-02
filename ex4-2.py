#ex4.2
s=input("输入一行字符串：")
county=counts=countk=countq=0
for i in s:
    if i.isalpha():
        county=county + 1
    elif i.isdigit():
        counts=counts + 1
    elif i.isspace():
        countk=countk + 1
    else:
        countq=countq + 1
        print("英文字母{}个".format(county))
        print("数字{}个".format(counts))
        print("空格{}个".format(countk))
        print("其他字符{}个".format(countq))
