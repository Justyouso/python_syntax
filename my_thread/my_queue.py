# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-14 下午3:46

from queue import Queue
from threading import Thread
import time


class Student(Thread):
    def __init__(self, name, queue):
        super().__init__()
        self.name = name
        self.queue = queue

    def run(self):
        while True:
            msg = self.queue.get()
            print("name", self.name)
            print(msg)
            if msg == self.name:
                print("{}：到！".format(self.name))


class Teacher:
    def __init__(self, queue):
        self.queue = queue

    def call(self, student_name):
        print("老师：{}来了没".format(student_name))
        self.queue.put(student_name)


queue = Queue()
teacher = Teacher(queue=queue)
s1 = Student(name="小明", queue=queue)
s2 = Student(name="小亮", queue=queue)
s1.start()
s2.start()
print("开始点名-")
teacher.call('小亮')
time.sleep(1)
teacher.call('小明')
