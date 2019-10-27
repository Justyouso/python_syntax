# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-10-27 下午9:35

from functools import wraps


def wrapper(func):
    @wraps(func)
    def inner_function():
        pass

    return inner_function

@wrapper
def wrapped():
    pass

print(wrapped.__name__)