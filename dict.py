d = {'周杰伦':45,'周润发': 65,'周星驰':60}
print(d['周杰伦'])
print(d['周润发'])
print(d['周星驰'])

print('-------------------------------')

#向字典里放入一个新的元素
d['周华健'] = 62
print(d)

d['周华健'] = 68
print(d)

print('-------------------------------')


#如果key不存在，就会报错
#print(d['周建'])

print('-------------------------------')

#通过2种方法避免key不存在的错误

if '周建' in d:
    print(d['周建'])
else:
    print('周建不存在字典d中')


if d.get('周建') != None:
    print(d['周建'])
else:
    print('周建不存在字典d中')

print('-------------------------------')

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d)
d.pop('周星驰')
print(d)

print('-------------------------------1')

s = set([1,2,3])
print(s)

print('-------------------------------2')

#重复元素在set中会被自动过滤
s = set([1,1,2,2,3,3])
print(s)

print('-------------------------------3')

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s = set([1,2,3])
s.add(4)
print(s)

print('-------------------------------4')

#通过remove(key)方法可以删除元素：
s.remove(4)
print(s)

print('-------------------------------5')

#交集和并集运算
s1 = set([1,2,3])
s2 = set([3,4,5])
#交集运算
print(s1 & s2)
#并集运算
print(s1 | s2)








