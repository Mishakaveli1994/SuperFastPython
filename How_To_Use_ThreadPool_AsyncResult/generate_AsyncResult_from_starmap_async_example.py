# example of getting an AsyncResult via starmap_async()
from random import random
from time import sleep
from multiprocessing.pool import ThreadPool


def task(identifier, value):
    print(f"Task {identifier} executing with {value}")
    sleep(value)
    return value


if __name__ == "__main__":
    items = [(i, random()) for i in range(10)]
    with ThreadPool() as pool:
        result = pool.starmap_async(task, items)
        pool.close()
        pool.join()
