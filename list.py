import keyword

print(keyword.kwlist)

print('I\'m \"OK\"')

#a为整数
a = 1
# b为字符串
b = 'xyz'
#c为布尔值
c = True

print(a)
print(b)
print(c)


print('--------------------------')

#student的集合students
students = ['周建','周围','周瑜']
print(students)
#取集合中的第一个元素
#print(students[0])
print(students[-3])

#取集合中的第二个元素
#print(students[1])
print(students[-2])

#取集合中的第三个元素
#print(students[2])
print(students[-1])

#打印出集合的长度
print(len(students))

print('--------------------------')

#添加元素
students.append('周杰')
print(students)

#把元素插入到指定位置
students.insert(1,'周杰伦')
print(students)

#删除集合末尾的元素
students.pop()
print(students)

#删除指定位置的元素
students.pop(1)
print(students)

#把某个元素替换成别的元素
students[1] = '周润发'
print(students)


print('--------------------------')

#list元素的数据类型可以不同

lists = ['周建',45,True]
print(lists)

print('--------------------------')

#list元素也可以是另一个list
s = ['Python',['Android','iOS'],'Java']
print(s)
print(len(s))

print('--------------------------')

a = ('a','b','c')
print(a)
b = ('a','b',['A','B'])
print(b[2][0])
print(b[2][1])






