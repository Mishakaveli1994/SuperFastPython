# example of executing a coroutine using the event loop
import asyncio


async def custom_coro(message):
    print(message)


asyncio.run(custom_coro("Hi from a coroutine"))
