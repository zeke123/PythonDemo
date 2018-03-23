#StringIO:在内存中读写str
from io import StringIO
f = StringIO()


print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
#getValue()方法用于获取写入的str
print(f.getvalue())

print('-----------------------1')

#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

print('-----------------------2')
#BytesIO
#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO

from io import BytesIO

f = BytesIO()
print(f.write('中国'.encode('utf-8')))
print(f.getvalue())

#和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
print('-----------------------3')
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')

print(f.read())