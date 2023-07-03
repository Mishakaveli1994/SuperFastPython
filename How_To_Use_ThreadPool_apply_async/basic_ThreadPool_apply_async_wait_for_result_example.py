# example of issuing a task with apply_async() and wait for result
from time import sleep
from random import random
from multiprocessing.pool import ThreadPool


def task():
    value = random()
    print(f"Task generated value {value}")
    sleep(1)
    print(f"Task done with value {value}")
    return value


if __name__ == "__main__":
    pool = ThreadPool()
    result = pool.apply_async(task)
    value = result.get()
    print(f"Got: {value}")
    pool.close()
