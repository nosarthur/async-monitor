import time

tic = time.monotonic()


def check_health(i):
    print(f'check health {i} @{time.monotonic() - tic:0.1f}')
    time.sleep(2 * i)


def main():
    while True:
        check_health(1)
        check_health(2)
        check_health(3)


if __name__ == '__main__':
    main()
