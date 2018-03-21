#要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs
print(abs(100))
print(abs(-10))
print(abs(-3.14))

print('---------------------1')

#max函数max()可以接收任意多个参数，并返回最大的那个：

print(max(1,3))
print(max(1,0,-1))

print('---------------------2')

#Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
#数据类型转换


int('123')
print(int('123'))

str(123)
print(str(123))

float('3.14')
print(float('3.14'))

bool(0)
print(bool(0))

bool(1)
print(bool(1))


print('---------------------3')

#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
#然后，在缩进块中编写函数体，函数的返回值用return语句返回。

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('允许整数和浮点数类型的参数')
    if x>= 0:
        return x
    else:
        return -x


print(my_abs(-99))
#print(my_abs('a'))



#空函数
#如果想定义一个什么事也不做的空函数，可以用pass语句：

def empty():
    pass


print('---------------------4')

#返回多个值

def func(x,y,z):
    nx = x+1
    ny = y+1
    nz = z+1
    return nx,ny,nz

x,y,z = func(1,2,3)

print(x,y,z )


print('---------------------5')

#位置参数，写一个计算x平方的函数

def power(x):
    return x * x

print(power(6))



def power(x,n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s

print(power(2,2))

print('---------------------6')

#默认参数

def power(x,n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3))

print('---------------------7')

def enroll(name,gender):
    print('name=',name)
    print('gender=',gender)

enroll('zhoujian','男')

print('---------------------8')


def enroll(name,gender,age = 26,city = '北京'):
    print('name=', name)
    print('gender=', gender)
    print('age=', age)
    print('city=', city)

enroll('zhoujian','男')


print('---------------------8')

enroll('zhoujian','男',30)

print('---------------------9')

enroll('zhoujian','男',age = 28,city = '上海')

print('---------------------10')

#可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


calc(1,2,3,4)
print(calc(1,2,3,4))

print('---------------------11')

#关键字参数

def person(name,age,**keyword):
    print('name=',name,'age=',age,'keyword=',keyword)

person("zhoujian",25)
person("zhoujian",25,city='北京')
person("zhoujian",25,city='北京',jop='程序员')
person("zhoujian",25,city='北京',jop='程序员',birthday = '1990年')

print('---------------------12')

#命名关键字参数

def person(name,age,**keyword):
    if 'city' in keyword:
        print('有city参数')

    if 'job' in keyword:
        print('有job参数')

    print('name=', name, 'age=', age, 'keyword=', keyword)

person("zhoujian",25)
person("zhoujian",25,city='北京')
person("zhoujian",25,job='程序员')

print('---------------------13')

#递归函数

def func(n):
    if n ==1:
        return 1
    return n * func(n-1)


print(func(5))




