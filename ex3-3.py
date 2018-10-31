#ex3.3
dayup,dayfactor,dayupa = 1,0.01,1
for i in range(365):
    if i% 11 in [3,4,5,6]:
        dayup = dayup * (1+dayfactor)
    else:
        dayup = dayup
print("10天休息一次的能力值:{:.2f}".format(dayup))
for i in range(365):
    if i% 16 in [3,4,5,6,7,11,12,13,14]:
        dayup = dayup * (1+dayfactor)
    else:
        dayup = dayup
print("15天休息一次的能力值:{:.2f}".format(dayup))
