# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-19 上午10:13

import asyncio


async def hello(name):
    print('Hello', name)


coroutine = hello("world")

loop = asyncio.get_event_loop()

task = loop.create_task(coroutine)
loop.run_until_complete(task)
