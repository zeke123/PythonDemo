from functools import reduce

#变量可以指向函数

x = abs(-10)
print('x=',x)


f = abs
y = (-10)
print('y=',y)

print('------------------------1')


#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数
# ，这种函数就称之为高阶函数。
#一个简单的高阶函数

def add(x,y,f):
    return f(x)+f(y)

s = add(-1,4,abs)

print('s=',s)

print('------------------------2')

#map/reduce
#Python内建了map()和reduce()函数。

#map()函数接受2个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

def f(x):
    return x * x

map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

print('------------------------3')
map(str,[1,2,3,4,5])
print(list(map(str,[1,2,3,4,5])))

print('------------------------4')
#reduce
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(x,y):
    return x + y


s= reduce(add ,[1,3,5,7,9])
print('s=',s)



def fn(x,y):
    return x *10 + y
s = reduce(fn,[1,3,5,7,9])
print('s=',s)

print('------------------------5')

#Python内建的filter()函数用于过滤序列。

#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

#在一个list中，删掉偶数，只保留奇数

def is_odd(n):
    return n % 2 == 1
filter(is_odd,[1,2,3,4,5,6,7,8,9,10])
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10])))


print('------------------------6')
#把一个序列中的空字符串删掉

def not_empty(s):
    return s and s.strip()

list(filter(not_empty,['1','','2',None,'3']))
print(list(filter(not_empty,['1','','2',None,'3'])))


print('------------------------7')

#排序算法
#Python内置的sorted()函数就可以对list进行排序：
sorted([1,-5,4,-9,10])
print(sorted([1,-5,4,-9,10]))


print('------------------------8')


#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：

sorted([1,-5,4,-9,10],key=abs)
print(sorted([1,-5,4,-9,10],key=abs))


print('------------------------9')

sorted(['about', 'bob', 'Zoo', 'Credit'])
print(sorted(['about', 'bob', 'Zoo', 'Credit']))

#忽略大小写
sorted(['about', 'bob', 'Zoo', 'Credit'],key= str.lower)
print(sorted(['about', 'bob', 'Zoo', 'Credit'],key= str.lower))

