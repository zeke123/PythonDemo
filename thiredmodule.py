#Pillow
#安装pip  sudo easy_install pip
#安装Pillow  sudo pip install pillow

#操作图像
import chardet
from PIL import Image
#打开一个图像文件m
im = Image.open('/Users/zhoujian/Desktop/text.jpg')
#获取图片尺寸
w,h = im.size
print('Original image size:%sx%s' % (w,h))
#缩放50%
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('/Users/zhoujian/Desktop/thumbnail.jpg', 'jpeg')


#模糊效果

from PIL import Image,ImageFilter

#打开一个图像文件m
im = Image.open('/Users/zhoujian/Desktop/text.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('/Users/zhoujian/Desktop/blur.jpg', 'jpeg')

#生成字母验证码图片

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
#随机字母
def rndChar():
    return chr(random.randint(65,90))

#随机颜色
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('/Users/zhoujian/Desktop/code.jpg', 'jpeg')

print('-----------------------1')

#requests
#已经讲解了Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。
#更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便
#安装requests   pip install requests
#使用requests
import requests
r = requests.get('https://www.baidu.com/')
print(r.status_code)
#print(r.text)

print('-----------------------2')
#对于带参数的URL，传入一个dict作为params参数：
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.status_code)
print(r.url)
print(r.encoding)
#print(r.text)
print('-----------------------3')

r = requests.get('https://api.douban.com/v2/book/2129650')
r.json()
print(r.json())

print('-----------------------4')

#要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
r = requests.post('http://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r.status_code)
print(r.url)
#print(r.text)


#如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
#url = 'https://accounts.douban.com/login'
#r = requests.post(url, json=params) # 内部自动序列化为JSON

#类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
#upload_files = {'file': open('report.xls', 'rb')}
#r = requests.post(url, files=upload_files)

#要指定超时，传入以秒为单位的timeout参数：
#r = requests.get(url, timeout=5)  # 5秒后超时

#chardet :用于检测编码
#安装chardet  pip install chardet
#当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码，只需要一行代码：
print('-----------------------5')
chardet.detect(b'Hello, world!')
print(chardet.detect(b'Hello, world!'))
#{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
#检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）

print('-----------------------6')
data = '举头望明月，低头思故乡'.encode('gbk')
print(chardet.detect(data))

print('-----------------------7')
data = '举头望明月，低头思故乡'.encode('utf-8')
print(chardet.detect(data))
print('-----------------------8')

#psutil
#它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，
#是系统管理员和运维小伙伴不可或缺的必备模块
#安装psutil：    sudo pip install psutil

#获取CPU信息
import psutil
psutil.cpu_count() # CPU逻辑数量
print(psutil.cpu_count())
# CPU物理核心
print(psutil.cpu_count(logical= False))

print('-----------------------9')

#统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())

print('-----------------------10')
#获取物理内存
print(psutil.virtual_memory())
#获取交换内存
print(psutil.swap_memory())

print('-----------------------11')

#获取磁盘信息
#磁盘分区信息
print(psutil.disk_partitions())
#磁盘使用情况
print(psutil.disk_usage('/'))

#磁盘IO
print(psutil.disk_io_counters())