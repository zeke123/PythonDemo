from collections import Iterable
#字典 是可迭代的对象
d = {'a':1,'b':2,'c':3}
for key in d:
    print('key=',key)

#字符串也是可迭代的对象

print('---------------------1')

for s in 'abcd':
    print('s=',s)

print('---------------------2')

#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

isinstance('abc',Iterable) #String 是否可迭代
print(isinstance('abc',Iterable))


isinstance(['a','b','c'],Iterable) #list 是否可迭代
print(isinstance(['a','b','c'],Iterable))


isinstance(('1','2','3'),Iterable) #tuple是否可迭代
print(isinstance(('1','2','3'),Iterable))

isinstance(123,Iterable) #整数是否可迭代
print(isinstance(123,Iterable))

print('---------------------3')

#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身


for i,value in enumerate(['a','b','c']):
    print('i=',i,'value=',value)

print('---------------------4')

for x,y in [(1,2),(2,4),(3,9)]:
    print(x,y)
