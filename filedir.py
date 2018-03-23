#操作文件和目录
import os
print(os.name)
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

print('------------------------1')

#要获取详细的系统信息，可以调用uname()函数：

print(os.uname())
print('------------------------2')

#环境变量
#在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：

print(os.environ)
print('------------------------3')
#要获取某个环境变量的值，可以调用os.environ.get('key')：

os.environ.get('PATH')

print(os.environ.get('PATH'))

#操作文件和目录
#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
#查看当前目录的绝对路径
os.path.abspath('.')

print(os.path.abspath('.'))
print('------------------------4')
#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/zhoujian/Python','hellodir')

print(os.path.join('/Users/zhoujian/Python','hellodir'))

print('------------------------5')

#然后创建一个目录:
#os.mkdir('/Users/zhoujian/Python/text')

print('------------------------6')
#os.rmdir('/Users/zhoujian/Python/hellodir')

#os.path.split('/Users/zhoujian/Python/text/zhoujian.txt')

#print(os.path.split('/Users/zhoujian/Python/text/zhoujian.txt'))

print('------------------------7')

#print(os.path.splitext('/Users/zhoujian/Python/text/zhoujian.txt'))

print('------------------------8')
#对文件重命名:

#os.rename('/Users/zhoujian/Python/text/哈哈哈.txt', '/Users/zhoujian/Python/text/zhoujian.txt')

#删除文件
#os.remove('/Users/zhoujian/Python/text/zhoujian.txt')


print([x for x in os.listdir('.') if os.path.isdir(x)])




