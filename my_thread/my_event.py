# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-5 下午8:47

import time
import threading


class MyThread(threading.Thread):
    def __init__(self, name, event):
        super().__init__()
        self.name = name
        self.event = event

    def run(self):
        print(
            'Thread: {} start at {}'.format(self.name, time.ctime(time.time())))
        # 等待event.set()后，才能往下执行
        self.event.wait()
        print('Thread: {} finish at {}'.format(self.name,
                                               time.ctime(time.time())))


if __name__ == "__main__":
    event = threading.Event()

    # 定义五个线程
    threads = [MyThread(str(i), event) for i in range(1, 5)]

    # 重置event，使得event.wait()起到阻塞作用
    event.clear()

    # 启动所有线程
    [t.start() for t in threads]

    print('等待5s...')
    time.sleep(5)

    print('唤醒所有线程...')
    event.set()
