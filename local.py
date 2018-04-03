import threading
#创建全局的ThreadLocal对象：

#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
#ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
local = threading.local()
def process_student():
    # 获取当前线程关联的student:
    std = local.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('xiao ming',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('xiao hong',),name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()
