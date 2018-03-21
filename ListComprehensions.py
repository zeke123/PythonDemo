
#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式

#生成一个list，从1-11 包括1，不包括11 就是1-10
list(range(1,11))
print(list(range(1,11)))


print('-------------------------1')

#把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
[x * x for x in range(1,11)]
print([x * x for x in range(1,11)])

print('-------------------------2')

#for循环后面还可以加上if判断
[x * x for x in range(1,11) if x % 2 ==0]
print([x * x for x in range(1,11) if x % 2 ==0])

print('-------------------------3')

#两层循环

[m + n for m in 'abc' for n in 'xyz']
print([m + n for m in 'abc' for n in 'xyz'])

print('-------------------------4')
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：

d = {'x': 'A', 'y': 'B', 'z': 'C' }

for k , v in d.items():
    print(k,'=',v)

print('-------------------------5')
#列表生成式也可以使用两个变量来生成list：

[k+'='+v for k,v in d.items()]

print([k+'='+v for k,v in d.items()])


print('-------------------------6')
#把一个list中所有的字符串变成小写：
s = ['ANDROID','JAVA','PYTHON']

[a.lower() for a in s]
print([a.lower() for a in s])

print('-------------------------7')
#isinstance函数可以判断一个变量是不是字符串：

x = 'abc'
y = 123
print(isinstance(x, str))
print(isinstance(y, str))






