# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-20 上午11:01
"""
运算阶乘
"""

import asyncio
import time


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print("Task {}: Compute factorial({})..".format(name, i))
        await asyncio.sleep(1)
        f *= i
    print("Task {}: factorial({}) = {}".format(name, number, f))


print(time.ctime())

tasks = [
    asyncio.ensure_future(factorial("A", 2)),
    asyncio.ensure_future(factorial("B", 3)),
    asyncio.ensure_future(factorial("C", 4)),
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))

print(time.ctime())
