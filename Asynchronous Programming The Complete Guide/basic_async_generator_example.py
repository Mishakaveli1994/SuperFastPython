# example of asynchronous generator with async for loop
import asyncio


async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield i


async def main():
    async for item in async_generator():
        print(item)


asyncio.run(main())
