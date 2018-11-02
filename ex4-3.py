#ex4.3
a,b=eval(input("输入两个整数："))
c=g=0
if a>b:
    a,b=b,a
while a%b!=0:
    c=a%b
    a=b
    b=c
g=int(a*b/c)
print("最小公约数是{}\n最大公倍数是{}".format(c,g))
