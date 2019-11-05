# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-5 下午9:12

"""
使用condition实现捉迷藏
"""

import threading, time


class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        # 确保先运行Hider
        time.sleep(1)
        self.cond.acquire()
        print(self.name + ": 我已经把眼睛蒙好了")
        self.cond.notify()
        self.cond.wait()
        print(self.name + ": 我找到你了")
        self.cond.notify()
        self.cond.release()
        print(self.name + ": 我赢了")


class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()
        print(self.name + ": 我已经藏好了")
        self.cond.notify()
        self.cond.wait()
        self.cond.release()
        print(self.name + ": 被你找到了")


if __name__ == "__main__":
    cond = threading.Condition()
    seeker = Seeker(cond, "seeker")
    hider = Hider(cond, "hider")
    hider.start()
    seeker.start()
