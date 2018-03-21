
import functools

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：

f = lazy_sum(1, 3, 5, 7, 9)
print(f())

print('---------------------1')
#调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)

print('---------------------2')

#注意到返回的函数在其定义内部引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 所以，闭包用起来简单，实现起来可不容易。

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

print('---------------------3')
#匿名函数
#在Python中，对匿名函数提供了有限支持。还是以map()函数为例，
# 计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：

map(lambda x: x*x,[1,2,3,4,5,6,7,8,9])

print(list(map(lambda x: x*x,[1,2,3,4,5,6,7,8,9])))

#匿名函数lambda x: x * x实际上就是：

def f(x):
    return x * x

#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

f = lambda x: x*x
print(f(5))

#同样，也可以把匿名函数作为返回值返回，比如：

def build(x, y):
    return lambda: x * x + y * y


f = build(2,2)
print(f())

print('---------------------4')


#装饰器
#在代码运行期间动态增加功能的方式，称之为“装饰器”（（Decorator）


def now():
    print('2018-03-16')

f = now
f()

#函数对象有一个__name__属性，可以拿到函数的名字：

now.__name__
f.__name__

print(now.__name__)
print(f.__name__)

print('---------------------5')
#在代码运行期间动态增加功能的方式，称之为“装饰器”（（Decorator）




#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）

#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：

int('12345')
print(int('12345'))

#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：

#转换为八进制
int('12345', base=8)
print(int('12345', base=8))

#转换为十六进制
int('12345',base=16)
print(int('12345',base=16))


print('---------------------6')

def int2(x, base=2):
    return int(x, base)

int2('1000000')
print(int2('1000000'))
int2('1010101')
print(int2('1010101'))

print('---------------------7')

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：

int3 = functools.partial(int , base = 2)
int3('1000000')
print(int3('1000000'))
int3('1010101')
print(int3('1010101'))