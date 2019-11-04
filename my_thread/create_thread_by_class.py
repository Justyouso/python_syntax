# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-4 下午9:18

"""
使用类实现线程
"""

import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name="Python"):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(2):
            print("hello", self.name)
            time.sleep(1)


if __name__ == "__main__":
    thread_01 = MyThread()
    thread_02 = MyThread("MING")
    thread_01.start()
    thread_02.start()
