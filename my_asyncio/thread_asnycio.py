# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-19 下午8:57

import asyncio
import time
from queue import Queue
from threading import Thread


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do_sleep(x, queue, msg=""):
    # time.sleep(x)
    await asyncio.sleep(x)
    queue.put(msg)


queue = Queue()
new_loop = asyncio.new_event_loop()

t = Thread(target=start_loop, args=(new_loop,))
t.start()

print(time.ctime())
#
# new_loop.call_soon_threadsafe(do_sleep, 6, queue, "one")
# new_loop.call_soon_threadsafe(do_sleep, 3, queue, "two")

asyncio.run_coroutine_threadsafe(do_sleep(6,queue,"one"),new_loop)
asyncio.run_coroutine_threadsafe(do_sleep(3,queue,"two"),new_loop)


while True:
    msg = queue.get()
    print("{} 协程运行完..".format(msg))
    print(time.ctime())
