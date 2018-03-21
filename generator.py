l = [x for x in range(0,10)]
print(l)

print('----------------------1')

g = (x for x in range(0,10))

#创建L和g的区别仅在于最外层的[]和()，l是一个list，而g是一个generator。
#可以通过next()函数获得generator的下一个返回值：
#print(next(g))

g = (x for x in range(0,3))

for n in g:
    print(n)

print('----------------------2')

#斐波那契数列

def fib(max):
    n = 0
    a = 0
    b = 1
    # n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

print('----------------------3')

#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)

print(f)

print('----------------------4')
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

