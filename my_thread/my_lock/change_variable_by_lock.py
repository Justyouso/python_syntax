# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-4 下午9:47

"""
加锁使用线程改变同一个变量
"""

from threading import Thread, Lock


def job1():
    # 因为需要改变全局变量
    global n, lock
    lock.acquire()
    for i in range(10):
        n += 1
        print("job1", n)
    lock.release()


def job2():
    # 因为需要改变全局变量
    global n, lock
    lock.acquire()
    for i in range(10):
        n += 10
        print("job2", n)
    lock.release()


if __name__ == "__main__":
    n = 0
    lock = Lock()

    t1 = Thread(target=job1)
    t2 = Thread(target=job2)
    t1.start()
    t2.start()
