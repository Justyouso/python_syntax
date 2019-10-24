# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-10-23 上午11:23


class logger(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]: {func} 正在运行...".format(level=self.level,
                                                     func=func.__name__))
            func(*args, **kwargs)

        return wrapper


@logger(level='WARNING')
def say(something):
    print("say {}!".format(something))


def say_without_decorator(something):
    print("say {}!".format(something))


if __name__ == '__main__':
    print("======= 类装饰器调用 =======")
    say("你好!")
    print("======= 未用类装饰器调用 =======")
    # 1.实例化logger
    logger_say_without_decorator = logger(level='DEBUG')
    # 2.传入func,调用__call__方法,返回wrapper
    wrapper = logger_say_without_decorator(say_without_decorator)
    # 3.执行wrapper函数,执行func函数
    wrapper("Hello")
