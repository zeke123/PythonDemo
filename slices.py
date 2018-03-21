students = ['周建','周峰','周杰','周成','周围']
#取前3个元素,索引包括0，不包括3
students[0:3]
print(students[0:3])

print('----------------------1')

#取出索引为1、2的元素
students[1:3]
print(students[1:3])

print('----------------------2')

#取出倒数第一个元素
students[-1]
#取出倒数第二个元素
students[-2]
print(students[-1])
print(students[-2])

print('----------------------3')
#取出倒数2个元素
print(students[-2:])
#取出倒数第二个元素和倒数第一个元素，不包括倒数第一个元素
print(students[-2:-1])

print('----------------------4')

#包括0 不包括100
print(range(100))
#转化为0-99的list
list(range(100))
print(list(range(100)))

print('----------------------5')

lists = list(range(0,100))
lists[0:10]
#取出0-10   包括0，不包括10
print(lists[0:10])


#前11-20个数 包括10，不包括20
print(lists[11:20])


print('----------------------6')

#取出0-10  包括0, 不包括10  每隔2个取一个
print(lists[0:10:2])

#每隔5个取一个
print(lists[::5])

print('----------------------7')
#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：

tu = (1,2,3,4,5,6,7,8,9)
print(tu[0:3])

print('----------------------8')
#字符串也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
str = 'asdfghjkl'
print(str[0:5])


