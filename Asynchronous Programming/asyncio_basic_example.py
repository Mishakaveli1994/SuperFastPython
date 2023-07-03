# example of asynchronous programming with asyncio

import asyncio


async def task_coroutine():
    print("Hello from the task")
    await asyncio.sleep(1)
    print("The task is all done")


async def main():
    # create the task coroutine
    coro = task_coroutine()
    # wrap in the task object and schedule execution
    task = asyncio.create_task(coro)
    # suspend a moment to allow the task to run
    await asyncio.sleep(0)
    # do other things, like report a message
    print("Main is doing other things...")
    # wait for the task to complete
    await task


# entry point into the program
asyncio.run(main())
