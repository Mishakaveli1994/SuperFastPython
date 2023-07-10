# example of executing a command as a subprocess with asyncio
import asyncio


async def main():
    # Can be made to read process input and reroute stdin, stdout and stderr
    process = await asyncio.create_subprocess_exec("echo", "Hello, world!")
    print(f"subprocess: {process}")


asyncio.run(main())
