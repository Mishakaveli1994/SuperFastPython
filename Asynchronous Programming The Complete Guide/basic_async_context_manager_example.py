# example of an asynchronous context manager via async with
import asyncio


class AsyncContextManager:
    async def __aenter__(self):
        print(f">entering the context manager")
        await asyncio.sleep(0.5)

    async def __aexit__(self, exc_type, exc_value, tb):
        print(f">exiting the context manager")
        await asyncio.sleep(0.5)


async def custom_coroutine():
    async with AsyncContextManager() as manager:
        print(f"within the manager")


asyncio.run(custom_coroutine())
