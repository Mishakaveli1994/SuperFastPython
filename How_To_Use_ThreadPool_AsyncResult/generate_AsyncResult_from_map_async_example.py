# example of getting an AsyncResult via map_async()
from random import random
from time import sleep
from multiprocessing.pool import ThreadPool


def task(identifier):
    value = random()
    print(f"Task {identifier} executing with {value}")
    sleep(value)
    return value


if __name__ == "__main__":
    with ThreadPool() as pool:
        result = pool.map_async(task, range(10))
        pool.close()
        pool.join()
