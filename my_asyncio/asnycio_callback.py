# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-19 上午10:42

"""
协程完整的工作流程是这样的 - 定义/创建协程对象 - 将协程转为task任务 - 定义事件循环对象容器 - 将task任务扔进事件循环对象中触发
回调函数，当协程执行完，调用其结果再进行同步编程
"""

import asyncio
import time


async def _sleep(x):
    time.sleep(2)
    return "暂停了{}秒".format(x)


def callback(future):
    print("这里是回调函数，获取返回结果是：", future.result())


# 创建协程
coroutine = _sleep(2)
# 定义事件循环对象容器
loop = asyncio.get_event_loop()
# 将协程转为task对象
task = asyncio.ensure_future(coroutine)
# 添加回调函数
task.add_done_callback(callback)
# 将task任务扔进事件循环对象中并触发
loop.run_until_complete(task)

print("返回结果：{}".format(task.result()))
