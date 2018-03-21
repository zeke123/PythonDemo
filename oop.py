
import requests
import types

#类和实例

#面向对象最重要的概念就是类（Class）和实例（Instance）
#必须牢记类是抽象的模板，比如Student类，
#而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同

#定义类是通过class关键字：

class Student(object):
    pass

#class后面紧接着是类名，即Student,类名通常是大写开头的单词

#(object)，表示该类是从哪个类继承下来的，这是所有类最终都会继承的类。

#定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：

student = Student()
print(student)

#可以自由地给一个实例变量绑定属性，比如，给实例student绑定一个name属性：
student.name = 'zhoujian'
print(student.name)

print('--------------------------1')


#通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

#注意到__init__方法的第一个参数永远是self,就可以把各种属性绑定到self，因为self就指向创建的实例本身。
class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score


student = Student('周建','90')
print(student.name)
print(student.score)

def print_message(student):

    print('%s:%s' % (student.name,student.score))


print_message(student)

print('--------------------------2')

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_message(self):
        print('%s: %s' % (self.name, self.score))



student = Student('zhoujian','50')

student.print_message()

print('--------------------------3')
#访问限制

#Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
#在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）
#只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

        def print_score(self):
            print('%s: %s' % (self.__name, self.__score))

bart = Student('Bart Simpson', 59)
#改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：

#bart.__name
#print(bart.__name)


#但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：



class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


student = Student('zhoujian',60)


student.get_name()
student.get_score()


print(student.get_name())
print(student.get_score())


student.set_name('周杰伦')
student.set_score(90)

student.print_score()


print('--------------------------4')

#继承和多态
#在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承
#新的class称为子类（Subclass），而被继承的class称为基类、父类或超类


class Animal(object):

    def run(self):
        print('Animal is running')


#dog 继承Animal
class Dog(Animal):
    pass

#cat 继承 Animal
class Cat(Animal):
    pass


#Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类
dog = Dog()
dog.run()


print('--------------------------5')


class Dog(Animal):
    def run(self):
        print('Dog is running')

    def eat(self):
        print('eating meat')

class Cat(Animal):
    def run(self):
        print('Cat is running')

    def eat(self):
        print('eating fish')



dog = Dog()
dog.run()
dog.eat()
print('--------------------------6')
cat = Cat()
cat.run()
cat.eat()


#当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()
#这样，我们就获得了继承的另一个好处：多态。

a = list() # a是list类型

b = Animal() # b是Animal类型

c = Dog() # c是Dog类型

print('--------------------------7')

#判断一个变量是否是某个类型可以用isinstance()判断：
isinstance(a,list)
print(isinstance(a,list))

isinstance(b,Animal)
print(isinstance(b,Animal))

isinstance(c,Dog)
print(isinstance(c,Dog))

isinstance(c,Animal)
print(isinstance(c,Animal))


print('--------------------------8')

#获取对象信息

#使用type()

#首先，我们来判断对象类型，使用type()函数：

type(123)
print(type(123))
print(type('abc'))
print(type(None))

#如果一个变量指向函数或者类，也可以用type()判断：

print(type(abs))

print('--------------------------9')

#type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断
#就需要比较两个变量的type类型是否相同：



print(type(123)== type(345))

print(type(123) == int)

print(type('abc') == type('123'))

print(type('abc') == str)

print(type('abc') == type(123))

print('--------------------------10')

#如果要判断一个对象是否是函数，可以使用types模块中定义的常量：

def fn():

    pass

type(fn) == types.FunctionType
print(type(fn) == types.FunctionType)

type(abs) == types.BuiltinFunctionType
print(type(abs) == types.BuiltinFunctionType)


type(lambda x:x) == types.LambdaType
print(type(lambda x:x) == types.LambdaType)

type(x for x in range(10)) == types.GeneratorType
print(type(x for x in range(10)) == types.GeneratorType)

print('--------------------------11')


#使用ininstance（）
#我们要判断class的类型，可以使用isinstance()函数。


a = Animal()
d = Dog()

isinstance(a,Animal)
print(isinstance(a,Animal))


isinstance(d,Animal)
print(isinstance(d,Animal))

#能用type()判断的基本类型也可以用isinstance()判断：

print('--------------------------12')
print('a',str)
print(123,int)



#并且还可以判断一个变量是否是某些类型中的一种
#比如下面的代码就可以判断是否是list或者tuple：

isinstance([1,2,3],(list,tuple))
print(isinstance([1,2,3],(list,tuple)))

isinstance((1, 2, 3), (list, tuple))
print(isinstance((1, 2, 3), (list, tuple)))

print('--------------------------13')

#使用dir()

#如果要获得一个对象的所有属性和方法，可以使用dir()函数
#它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

dir('abc')
print(dir('abc'))

#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度
#在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部
#它自动去调用该对象的__len__()方法，所以，下面的代码是等价的

print(len('abc'))

print('abc'.__len__())

print('--------------------------14')
#lower()返回小写的字符串：

print('ABC'.lower())

print('--------------------------15')
#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()
#我们可以直接操作一个对象的状态：

class MyObject(object):

    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

#有属性x吗

hasattr(obj,'x')
print(hasattr(obj,'x'))
print(obj.x)

#有属性y吗
hasattr(obj,'y')
print(hasattr(obj,'y'))


#设置属性y
setattr(obj,'y',12)
hasattr(obj,'y')
print(hasattr(obj,'y'))


#获取属性y

getattr(obj,'y')
print(getattr(obj,'y'))
print(obj.y)


print('--------------------------16')
#如果试图获取不存在的属性，会抛出AttributeError的错误：

#getattr(obj,'z')

#print(getattr(obj,'z'))


#可以传入一个default参数，如果属性不存在，就返回默认值：

getattr(obj, 'z', 404)
print(getattr(obj, 'z', 404))


print('--------------------------17')

#也可以获取对象的方法

#有属性'power'吗？
hasattr(obj,'power')
print(hasattr(obj,'power'))

#获取属性'power'
getattr(obj,'power')
print(getattr(obj,'power'))

#获取属性'power'并赋值到变量fn

fn = getattr(obj,'power')

print(fn())


print('--------------------------18')






#实例属性和类属性

#由于Python是动态语言，根据类创建的实例可以任意绑定属性

#给实例绑定属性的方法是通过实例变量，或者通过self变量

class Student(object):

    def __init__(self,name):
        self.name = name


s = Student('zhoujian')
a.score = 90
print(a.score)

#如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性
#这种属性是类属性，归Student类所有：

class Student(object):
    name = '周建'

#创建实例student
s = Student()
#打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(s.name)

#打印类的name属性
print(Student.name)

#给实例绑定name属性
s.name = '周杰伦'
#由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(s.name)

# 但是类属性并未消失，用Student.name仍然可以访问

print(Student.name)

#删除实例的name属性
del s.name
print(s.name)




















