# (1)读文件

f = open('/Users/zhoujian/Desktop/zhoujian.txt', 'r')
print(f.read())
f.close()

print('----------------------1')

#文件使用后必须关闭
try:
    f = open('/Users/zhoujian/Desktop/zhoujian.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

print('----------------------2')

#Python引入了with语句来自动帮我们调用close()方法：

with open('/Users/zhoujian/Desktop/zhoujian.txt', 'r') as f:
    print(f.read())

#调用read()会一次性读取文件的全部内容
#readline()可以每次读取一行内容
#调用readlines()一次读取所有内容并按行返回list
print('----------------------3')

f = open('/Users/zhoujian/Desktop/zhoujian.txt', 'r')
for lines in f.readlines():
    print(lines.strip()) # 把末尾的'\n'删掉

print('----------------------4')


#二进制文件
#前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件
#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

f = open('/Users/zhoujian/Desktop/demo.jpg','rb')
print(f.read())
f.close()

print('----------------------5')
#字符编码
f = open('/Users/zhoujian/Desktop/zhoujian.txt', 'r', encoding='gbk')
print(f.read())
f.close()

print('----------------------6')
#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError
#因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况
#open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理
#最简单的方式是直接忽略：

f = open('/Users/zhoujian/Desktop/zhoujian.txt', 'r', encoding='gbk', errors='ignore')
print(f.read())
f.close()

#(2)写文件
#写文件和读文件是一样的，唯一区别是调用open()函数时
#传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

f = open('/Users/zhoujian/Desktop/zhoujian.txt', 'w')
f.write('hello')
f.close()

#你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件

with open('/Users/zhoujian/Desktop/zhoujian.txt', 'w') as f:
    f.write('Hello, world!')



