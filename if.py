
from fuc import my_abs

my_abs(9)
print(my_abs(9))


a = 20
if a >= 18:
    print('你是个成年人，年龄是',a)
elif a < 18:
    print('你是个未成年人，年龄是',a)
else:
    print('你是个老年人,年龄是',a)


s = input('出生年：')
#把字符串转换成int
birth = int(s)
if birth < 2012:
    print('2012年前')
else:
    print('2012年后')

