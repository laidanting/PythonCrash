#encoding=utf-8

import queue, time, random
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()
#接收结果的队列
result_queue = queue.Queue()

#创建一个QueueManager类，从BaseManager继承
class QueueManager(BaseManager):
    pass

#将队列注册到网络上
QueueManager.register("get_task_queue", callable=lambda: task_queue)
QueueManager.register("get_result_queue", callable=lambda: result_queue)

#绑定端口5000，并设验证码abc
manager = QueueManager(address=('', 5000), authkey=b'abc')

#启动队列
manager.start()

#获得通过网络访问的队列对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#将任务放在task中
for i in range(10):
    n = random.randint(0, 10000)
    print 'Put task %d ...' % n
    task.put(n)

#从results中获取结果
print 'Try get results...'
for i in range(10):
    r = result.get(timeout=10)
    print 'Result: %s' % r

#关闭
manager.shutdown()
print 'master exit...'