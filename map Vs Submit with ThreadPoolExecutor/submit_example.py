# example of the submit and use as completed pattern for the ThreadPoolExecutor
from time import sleep, time
from random import random, randint
from concurrent.futures import ThreadPoolExecutor, as_completed


def task(name):
    # sleep(random())
    sleep_interval = randint(0, 10)
    # if sleep_interval == 3:
    #     raise Exception("Task Exception")
    sleep(sleep_interval)
    return f"{name} - {sleep_interval} seconds"


started = time()
with ThreadPoolExecutor(10) as executor:
    futures = [executor.submit(task, i) for i in range(10)]
    for future in as_completed(futures):
        print(future.result())
elapsed = time() - started

print(f'\nQueue time elapsed: {elapsed:.2f}s')
