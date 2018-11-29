"""
Requires python 3.7
"""
import asyncio
import time
from typing import Callable


now = time.monotonic()


async def run_at_interval(t: float, predicate: Callable):
    while True:
        await asyncio.sleep(t)
        print(f'check health {t}: @{time.monotonic() - now:0.1f}')
        feedback = predicate()
        if feedback:
            return feedback


async def main():
    all_good = lambda: False
    t1 = asyncio.create_task(run_at_interval(3, all_good))
    t2 = asyncio.create_task(run_at_interval(5, all_good))
    timeout = asyncio.create_task(asyncio.sleep(16))
    done, pending = await asyncio.wait({t1, t2, timeout},
                                       return_when=asyncio.FIRST_COMPLETED)
    for t in pending:
        t.cancel()
    feedback = await done.pop()
    return feedback


if __name__ == '__main__':
    #with closing(asyncio.get_event_loop()) as loop:
    #    loop.run_until_complete(main())
    asyncio.run(main())
