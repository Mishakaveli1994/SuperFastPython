# example of running a blocking io-bound task in asyncio
import asyncio
import time


def blocking_task():
    print("Task starting")
    time.sleep(2)
    print("Task done")


async def main():
    print("Main is running the blocking task")
    coro = asyncio.to_thread(blocking_task)
    task = asyncio.create_task(coro)
    print("Main doing other things")
    await asyncio.sleep(0)
    await task


asyncio.run(main())
