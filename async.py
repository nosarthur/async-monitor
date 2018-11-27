"""
Requires python 3.7
"""
import asyncio
import time
from typing import Callable
from contextlib import closing


now = time.monotonic()


async def run_at_interval(t: float, predicate: Callable):
    while True:
        print(f'check health {t}: @{time.monotonic() - now:0.1f}')
        if predicate():
            return
        await asyncio.sleep(t)


async def main():
    all_good = lambda: False
    t1 = asyncio.create_task(run_at_interval(3, all_good))
    t2 = asyncio.create_task(run_at_interval(5, all_good))
    t3 = asyncio.create_task(run_at_interval(7, all_good))
    timeout = loop.create_task(asyncio.sleep(23))
    done, pending = await asyncio.wait({t1, t2, t3, timeout},
                                       return_when=asyncio.FIRST_COMPLETED)
    for t in pending:
        t.cancel()
    x = await done.pop()
    return x


if __name__ == '__main__':
    with closing(asyncio.get_event_loop()) as loop:
        loop.run_until_complete(main())
