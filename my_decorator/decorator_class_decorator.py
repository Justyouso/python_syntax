# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-10-24 下午10:18
"""
单例模式
"""
instances = {}


def singleton(cls):
    def get_instance(*args, **kwargs):
        cls_name = cls.__name__
        if cls_name not in instances:
            instance = cls(*args, **kwargs)
            instances[cls_name] = instance
        return instances[cls_name]

    return get_instance


@singleton
class User:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    u1 = User('wc')
    u2 = User('dmq')
    print(u1 is u2)
