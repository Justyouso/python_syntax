# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-4 下午9:59

"""
如果第一次锁没有释放，就去再次获取锁，将会产生死锁，Rlock可以解决此类问题
"""

from threading import Thread, RLock, Lock


def obj_by_lock():
    n = 0
    lock = Lock()
    with lock:
        for i in range(10):
            n += 1
            with lock:
                print(n)


def obj_by_rlock():
    n = 0
    lock = RLock()
    with lock:
        for i in range(10):
            n += 1
            with lock:
                print(n)


if __name__ == "__main__":
    # 会产生死锁
    # t1 = Thread(target=obj_by_lock)
    # t1.start()

    # 正常执行
    t2 = Thread(target=obj_by_rlock)
    t2.start()
