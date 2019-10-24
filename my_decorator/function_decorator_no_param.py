# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-10-23 上午10:31
import time


def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print("花费时间:{}秒".format(t2 - t1))

    return wrapper


@timer
def want_sleep(sleep_time):
    time.sleep(sleep_time)


def want_sleep_without_decorator(sleep_time):
    time.sleep(sleep_time)


if __name__ == '__main__':
    print("======= 装饰器调用 =======")
    want_sleep(2)
    print("======= 未用装饰器调用 =======")
    timer(want_sleep_without_decorator)(2)
