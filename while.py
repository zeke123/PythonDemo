names = ['周润发','周杰伦','周星驰']
for name in names:
    print(name)

for name in ['周润发','周杰伦','周星驰']:
    print(name)

print('----------------------')
#计算1-10的和
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

print('----------------------')

#range() 函数可以生成一个整数序列
#通过list() 函数可以转换成list
list(range(6))
print(list(range(6)))

print('----------------------')

#这样计算0-100数字之和就方便多了
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

print('----------------------')

#While循环
#计算100以内所有奇数
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

print('----------------------')

#break语句可以提前退出循环
n = 1
while n <= 100:
    if n > 4:
        break #结束当前循环
    print(n)
    n = n + 1
print('结束')


print('----------------------')

#continue结束本次循环，继续下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: #如果n是偶数，执行continue语句
        continue
    print(n)


