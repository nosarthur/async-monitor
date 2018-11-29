import time
from typing import Callable


tic = time.monotonic()


def check_health(i: int, predicate: Callable) -> bool:
    """
    Return True if something goes wrong
    """
    print(f'check health {i} @{time.monotonic() - tic:0.1f}')
    return predicate()


def main():
    all_good = lambda: False
    while True:
        feedback = check_health(1, all_good)
        if feedback:
            break

        feedback = check_health(2, all_good)
        if feedback:
            break

        feedback = check_health(3, all_good)
        if feedback:
            break
        time.sleep(3)


if __name__ == '__main__':
    main()
