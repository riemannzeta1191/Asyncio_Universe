import asyncio
import random
import time


async  def foo():
    print("running in foo")
    await asyncio.sleep(0)
    print('context switch to foo again')

async def bar():
    print('explicit context switch to bar')
    await asyncio.sleep(0)
    print('implicit context switch to bar')


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()),ioloop.create_task(bar())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()

#asyncio

