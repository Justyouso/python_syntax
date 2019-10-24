# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-10-23 上午11:23


class logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[INFO]: {func} 正在运行...".format(func=self.func.__name__))
        return self.func(*args, **kwargs)


@logger
def say(something):
    print("say {}!".format(something))


def say_without_decorator(something):
    print("say {}!".format(something))


if __name__ == '__main__':
    print("======= 装饰器调用 =======")
    say("你好!")
    print("======= 未用装饰器调用 =======")
    # 1.实例化
    logger_say_without_decorator = logger(say_without_decorator)
    # 2.调用__call__方法
    logger_say_without_decorator("Hello")
