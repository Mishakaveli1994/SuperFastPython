# example of waiting for a coroutine with a timeout
from random import random
import asyncio


async def task_coro():
    value = 1 + random()
    print(f">task got value {value}")
    await asyncio.sleep(value)
    print(f">task done")


async def main():
    task = task_coro()
    try:
        await asyncio.wait_for(task, timeout=0.2)
    except asyncio.TimeoutError:
        print("Gave up waiting, task cancelled")


asyncio.run(main())
