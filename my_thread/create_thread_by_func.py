# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-4 下午5:42

"""
方法实现线程
"""

import time
from threading import Thread


def main(name="Python"):
    for i in range(2):
        print("hello", name)
        time.sleep(1)


thread_01 = Thread(target=main, name="Python")
thread_01.start()

thread_02 = Thread(target=main, args=("MING",), name="MING")
thread_02.start()
