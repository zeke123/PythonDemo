#collections是Python内建的一个集合模块，提供了许多有用的集合类。
from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p,Point))
print(isinstance(p,tuple))

print('----------------------1')

#deque
#使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了
#因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

from collections import deque
q = deque(['a','b','c'])
q.append('y')
print('q =',q)
q.appendleft('x')
print('q =',q)

print('----------------------2')

#defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。
#如果希望key不存在时，返回一个默认值，就可以用defaultdict：

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
#key2不存在，返回默认值
print(dd['key2'])

print('----------------------3')

#OrderedDict
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d)

od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))

print('----------------------4')
#Counter是一个简单的计数器，例如，统计字符出现的个数：

from collections import Counter
c = Counter()
for char in 'teacher':
    c[char] = c[char] + 1
print('c=',c)