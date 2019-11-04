# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-4 下午9:33

"""
不加锁使用线程改变同一个变量
"""

from threading import Thread


def job1():
    # 因为需要改变全局变量
    global n
    for i in range(10):
        n += 1
        print("job1", n)


def job2():
    # 因为需要改变全局变量
    global n
    for i in range(10):
        n += 10
        print("job2", n)


if __name__ == "__main__":
    n = 0

    t1 = Thread(target=job1)
    t2 = Thread(target=job2)
    t1.start()
    t2.start()
