# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-19 上午11:14

"""
协程并发
"""
import asyncio
import time


async def do_some_work(x):
    print('Waiting:', x)
    # 挂起阻塞的异步调用接口，也就是挂起当前任务，去执行其他任务
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


def callback(future):
    print('这里是回调函数，获取返回结果是：', future.result())


start = time.time()
# 协程对象
coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

# 将协程转为task
tasks = [asyncio.ensure_future(coroutine1), asyncio.ensure_future(coroutine2),
         asyncio.ensure_future(coroutine3)]
# 给task添加回调函数
for i in tasks:
    i.add_done_callback(callback)
# 定义事件循环对象容器
loop = asyncio.get_event_loop()
# 将tasks扔进事件循环对象容器并触发
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task result:', task.result())
end = time.time()
print(end - start)
