# example of using asyncio shield to protect a task from cancellation
import asyncio


async def simple_task(number):
    await asyncio.sleep(1)
    print("Heheh task is shielded")
    return number


async def cancel_task(task):
    await asyncio.sleep(0.2)
    was_cancelled = task.cancel()
    print(f"cancelled: {was_cancelled}")


async def main():
    coro = simple_task(1)
    task = asyncio.create_task(coro)
    shielded = asyncio.shield(task)
    asyncio.create_task(cancel_task(shielded))
    try:
        result = await shielded
        print(f">got: {result}")
    except asyncio.CancelledError:
        print('shielded was cancelled')
    await asyncio.sleep(1)
    print(f"shielded: {shielded}")
    print(f'task: {task}')


asyncio.run(main())
