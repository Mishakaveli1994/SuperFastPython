# access the current event loop
import asyncio

current_loop = asyncio.get_running_loop()
print(current_loop)
