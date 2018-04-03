#多线程
#Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，
# threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行

import time,threading
#新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n+1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop,name = 'LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

print('--------------------------1')

#，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

import time,threading
balance = 0

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thraad(n):
    for i in range(1000000):
        change_it(n)

t1 = threading.Thread(target=run_thraad,args=(5000,))
t2 = threading.Thread(target=run_thraad,args=(3000,))
t1.start()
t2.start()
t1.join()
t2.join()
print('balance=',balance)

print('--------------------------2')
# 如果我们要确保balance计算正确，就要给change_it()上一把锁
# 当某个线程开始执行change_it()时，我们说，该线程因为获得了锁
# 因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后
# 获得该锁以后才能改。由于锁只有一个，无论多少线程
# 同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突
# 创建一个锁就是通过threading.Lock()来实现：
import time,threading
balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thraad(n):
    for i in range(1000000):
        #先获取锁
        lock.acquire()
        try:
            #放心修改
            change_it(n)
        finally:
            #改完了一定要释放锁
            lock.release()

t1 = threading.Thread(target=run_thraad,args=(5000,))
t2 = threading.Thread(target=run_thraad,args=(3000,))
t1.start()
t2.start()
t1.join()
t2.join()
print('balance=',balance)

