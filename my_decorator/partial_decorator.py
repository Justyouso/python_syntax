# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-10-24 下午9:16

"""
使用偏函数与类实现装饰器
"""
import time
from functools import partial

class DelayFunc(object):
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} seconds...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay')
        return self.func(*args, **kwargs)


def delay_without_partial(duration):
    """
    装饰器: 推迟某个函数的执行
    同时提供 .eager_call 方法执行
    :param duration: 
    :return: 
    """

    def wrapper(func):
        return DelayFunc(duration=duration, func=func)

    return wrapper


def delay(duration):
    """
    装饰器: 推迟某个函数的执行
    同时提供 .eager_call 方法执行
    :param duration: 
    :return: 
    """
    # 直接使用偏函数帮助构造 DelayFunc 实例
    return partial(DelayFunc, duration)


@delay_without_partial(duration=2)
def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(1, 2))
    # 可直接调用类的方法
    print(add.eager_call(1, 2))
