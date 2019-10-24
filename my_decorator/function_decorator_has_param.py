# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-10-23 上午10:43

"""
带参数方法装饰器
"""


def say_hello(country):
    def wrapper(func):
        def deco(*args, **kwargs):
            if country == "china":
                print("你好!")
            else:
                print("Hello!")
            func(*args, **kwargs)

        return deco

    return wrapper


@say_hello(country="china")
def say_name(name):
    print("我叫:{}".format(name))


def say_name_without_decorator(name):
    print("我叫:{}".format(name))


if __name__ == '__main__':
    print("======= 装饰器调用 =======")
    say_name("小明")
    print("======= 未用装饰器调用 =======")
    # 1. 返回wrapper函数
    wrapper = say_hello(country="america")
    # 2. 返回deco函数
    deco = wrapper(say_name_without_decorator)
    # 3. 执行deco,执行func
    func = deco("jack")
