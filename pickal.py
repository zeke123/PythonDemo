# 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
d = dict(name='zhoujian', age=20, score=90)
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
# 把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
# Python提供两个模块来实现序列化：cPickle和pickle
# 这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢
# 用的时候，先尝试导入cPickle，如果失败，再导入pickle

try:
    import cPickle as pickle
except ImportError:
    import pickle

#把一个对象序列化并写入文件：
d = dict(name='zhoujian', age=20, score=90)
#pickle.dumps()方法把任意对象序列化成一个str,写进去
pickle.dumps(d)
print(pickle.dumps(d))
print('--------------------1')
f = open('zj.txt','wb')
pickle.dump(d,f)
f.close()
#读取出来
f = open('zj.txt','rb')
d = pickle.load(f)
f.close()
print(d)
#当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已

#JSON
#如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式
#比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串
#可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输
#JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
#JSON类型           Python类型
#  {}                dict
#  []                list
#String              str
#3.23                int或者float
#true/false          True/False
#null                None
#如何把Python对象变成一个JSON：
print('--------------------2')
import json
d = dict(name='zhoujian', age=20, score=90)
print(json.dumps(d))
print('--------------------3')
#要把JSON反序列化为Python对象
json_str = '{"name": "zhoujian", "age": 20, "score": 90}'
json.loads(json_str)
print(json.loads(json_str))
print('--------------------4')
#JSON进阶
#Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
s = Student('zhoujian',28,100)
#会发生错误  错误的原因是Student对象不是一个可序列化为JSON的对象
#print(json.dumps(s))
#可选参数default就是把任意一个对象变成一个可序列为JSON的对象
#我们只需要为Student专门写一个转换函数，再把函数传进去即可
def student2dict(stu):
    return {
        'name':stu.name,
        'age':stu.age,
        'score':stu.score
    }
#这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON。
print(json.dumps(s,default=student2dict))
print('--------------------5')
print(json.dumps(s,default=lambda obj:obj.__dict__))


