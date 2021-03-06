
import threading
import time
import random

# 线程锁：当有一个数据有多个线程可以对其进行修改的时候，任何一个线程
# 改变它都会被其他线程影响，如果我们一个线程在使用完之前，其他线程不能对其修改，就需要对这个线程增加一个线程锁、

count = 0
def get_money(money):
    global count
    count+=money
    count+=money
    count -= money
# 创建一个线程锁对象
lock = threading.Lock()
def lock_thread(money):
    # acquire 捕获
    # 加锁
    lock.acquire()
    time.sleep(random.randint(1,3))
    print('当前线程为',threading.current_thread().name)
    get_money(money)
    time.sleep(random.randint(1, 3))
    print('当前线程为', threading.current_thread().name)
    # 解锁
    lock.release()
# 创建线程的参数为一个元祖类型
# 主线程 开辟一个分线程
thread1 = threading.Thread(target=lock_thread,name='thread1',args=(1000,))
thread2 = threading.Thread(target=lock_thread,name='thread2',args=(2000,))
thread1.start()
thread2.start()
print('hello world')
# join 注重的整体 线程1没有执行完，线程2不能执行
# lock 注重的是局部  某一个变量没有用完，其他线程不能使用
thread1.join()
thread2.join()