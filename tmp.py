import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    t1 = asyncio.create_task(say_after(1, 'hello'))
    t2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    await t2
    await t1

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
