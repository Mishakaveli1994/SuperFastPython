# example of the map and wait pattern for ThreadPoolExecutor
from time import sleep, time
from random import random, randint
from concurrent.futures import ThreadPoolExecutor


def task(name):
    # sleep(random())
    # Testing purposes
    sleep_duration = randint(0, 6)
    sleep(sleep_duration)
    return f"{name} - {sleep_duration} seconds"


started = time()
with ThreadPoolExecutor(10) as executor:
    # important i that the order is retained
    for result in executor.map(task, range(10)):
        print(result)

elapsed = time() - started

print(f'\nQueue time elapsed: {elapsed:.2f}s')
