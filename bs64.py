import base64

# base64
base64.b64encode(b'zhoujian')
print(base64.b64encode(b'zhoujian'))

print(base64.b64decode(b'emhvdWppYW4='))

print('--------------------------1')

# struct
# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
# struct的pack函数把任意数据类型变成bytes：

import struct

struct.pack('>I', 678589)
print(struct.pack('>I', 678589))
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

print('--------------------------2')

# hashlib
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
import hashlib

md5 = hashlib.md5()
md5.update('zhou jian'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('zhou jian'.encode('utf-8'))
print(sha1.hexdigest())

print('--------------------------3')

# hmac
import hmac

message = b'Hello world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())

print('--------------------------4')

# itertools
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
# 看看itertools提供的几个“无限”迭代器：
import itertools

natuals = itertools.count(1)
# for n in natuals:
#      print(n)

cs = itertools.cycle('abc')
# for c in cs:
#     print(c)

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：

ns = itertools.repeat('A', 3)
for n in ns:
    print(n)
print('--------------------------5')
# 无限序列虽然可以无限迭代下去，
# 但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))
print('--------------------------6')
# itertools提供的几个迭代器操作函数更加有用：
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：

for c in itertools.chain('abc', 'xyz'):
    print(c)
print('--------------------------7')
# groupby()把迭代器中相邻的重复元素挑出来放在一起

for key, group in itertools.groupby('aavvccrrrr'):
    print(key, list(group))

print('--------------------------8')

from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('begin')
    q = Query(name)
    yield q
    print('end')


with create_query('zhoujian') as q:
    q.query()
print('--------------------------9')

# urllib提供了一系列用于操作URL的功能
# Get
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：

from urllib import request
import ssl

context = ssl._create_unverified_context()
with request.urlopen('https://api.douban.com/v2/book/2129650', context=context) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

print('--------------------------10')
# Post
from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8'), context=context) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

print('--------------------------11')

from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

print('--------------------------12')
# HTMLParser

from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
