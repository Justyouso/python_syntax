# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-14 下午4:44

from queue import PriorityQueue


# 重新定义一个类，继承自PriorityQueue
class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item


queue = MyPriorityQueue()
queue.put('item2', 2)
queue.put('item5', 5)
queue.put('item3', 3)
queue.put('item4', 4)
queue.put('item1', 1)
queue.put('item11', 1)
queue.put('item12', 1)

while True:
    print(queue.get())
