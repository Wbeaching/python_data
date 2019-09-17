


# queue 队列
import queue
# 创建一个线程队列
# 队列：FIFO  first in first out 先进先出
# q = queue.Queue()
# for i in range(5):
#     # 将内容放到线程队列中
#      q.put(i)
# while not q.empty():
#     # get 得到
#     print(q.get())
# Lifo last in first out 后进先出
p = queue.LifoQueue()
for i in range(5):
    p.put(i)
while not p.empty():
    print(p.get())
