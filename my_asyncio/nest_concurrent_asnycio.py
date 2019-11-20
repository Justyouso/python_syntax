# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-19 上午11:43

import asyncio


async def do_some_work(x):
    print('Waiting:', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    # 将协程转为task
    tasks = [asyncio.ensure_future(coroutine1),
             asyncio.ensure_future(coroutine2),
             asyncio.ensure_future(coroutine3)]

    dones, pendings = await asyncio.wait(tasks)
    for task in dones:
        print('Task result:', task.result())


# 定义事件循环对象容器
loop = asyncio.get_event_loop()
# 将task扔进事件循环对象容器
loop.run_until_complete(main())
