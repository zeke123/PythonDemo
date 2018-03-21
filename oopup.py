from types import MethodType

#面向对象高级编程

#(1)使用 __slots__
print('----------------------1')

#正常情况下，当我们定义了一个class，创建了一个class的实例后
#我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：

class Student(object):

    pass


#尝试给实例绑定一个属性：

s = Student()
s.name = '周建'
print(s.name)
print('------------------1.1')

#给实例绑定一个方法：

#首次定义一个方法

def set_age(self,age):

    self.age = age

#给实例绑定一个方法
s.set_age = MethodType(set_age,s)
s.set_age(28)
print(s.age)
print('------------------1.2')
#为了给所有实例都绑定方法，可以给class绑定方法

def set_score(self,score):
    self.score = score

Student.set_score = set_score

s1 = Student()
s1.set_score(100)
print(s1.score)
print('------------------1.3')

s2 = Student()
s2.set_score(99)
print(s2.score)
print('------------------1.4')


#使用__slots__
#如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：


class Student(object):
    #用tuple定义允许绑定的属性名称
    __slots__ = ('name','age')


#创建新的实例

s = Student()
s.name = '周建'
s.age = 28
#会报错  AttributeError: 'Student' object has no attribute 'score'
#s.score = 98
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：




#(2)使用@property
print('----------------------2')

#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：

class Student(object):

    pass

s = Student()

s.score = 200
print(s.score)
print('------------------2.1')

#这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩
#再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数

class Student(object):

    def get_score(self):
        return self._score

    def set_score(self,value):

        if not isinstance(value,int):

            raise ValueError('分数必须是整数')
        if value < 0 or value > 100:

            raise ValueError('分数必须在0-100之间')

        self._score = value


#现在，对任意的Student实例进行操作，就不能随心所欲地设置score了

s = Student()
s.set_score(80)
s.get_score()
print(s.get_score())

print('------------------2.2')

#报错s.set_score(200)

#Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Student(object):

    @property
    def score(self):
        return self._score


    @score.setter
    def score(self,value):

        if not isinstance(value,int):

            raise ValueError('分数必须是整数')
        if value < 0 or value > 100:

            raise ValueError('分数必须在0-100之间')

        self._score = value

#把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter
#负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

s = Student()
s.score = 60
print(s.score)



#(3)多重继承

#Dog - 狗狗； Bat - 蝙蝠；     Parrot - 鹦鹉；Ostrich - 鸵鸟。

#动物总称
class Animal(object):
    pass

#哺乳类动物
class Mammal(Animal):
    pass

#鸟类
class Bird(Animal):
    pass

#狗-哺乳动物
class Dog(Mammal):
    pass

#蝙蝠-哺乳动物
class Bat(Mammal):
    pass

#鹦鹉-鸟类
class Parrot(Bird):
    pass

#鸵鸟-鸟类
class Ostrich(Bird):
    pass


#现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：

#跑的属性

class Runnable(object):

    def run(self):
        print('Running....')

#飞的属性

class Flyable(object):

    def fly(self):
        print("Flaying....")


#对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：

#狗是能跑的动物，也是哺乳动物  多继承

class Dog(Mammal,Runnable):
    pass

#对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：

class Bat(Mammal,Flyable):
    pass

#通过多重继承，一个子类就可以同时获得多个父类的所有功能。



#MixIn
class Dog(Mammal,Runnable):
    pass


#狗除了继承哺乳动物Mammal外，同时还继承Runnable，这种设计称之为MixIn



#(4)定制类
print('----------------------4')

#__str__

class Student(object):

    def __init__(self,name):

        self.name = name

    def __str__(self):

        return 'Student object (name:%s)' % self.name

print(Student('周建'))

print('------------------4.1')

# __iter__


#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
#该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值
#直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 20: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值


for n in Fib():

    print(n)


print('------------------4.2')

#__getitem__

#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()

print(f[0])
print(f[1])
print(f[2])

print('------------------4.3')



#__getattr__
#动态返回一个属性































#(5) 使用枚举类
print('----------------------5')





#(6)使用元类
print('----------------------6')
