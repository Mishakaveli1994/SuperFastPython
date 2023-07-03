# example of issuing a task with apply_async() with a callback function to the thread pool
from time import sleep
from random import random
from multiprocessing.pool import ThreadPool


def return_callback(result):
    print(f"Callback received: {result}")


def task():
    value = random()
    print(f"Task generated value {value}")
    sleep(1)
    print(f"Task done with value {value}")
    return value


if __name__ == "__main__":
    pool = ThreadPool()
    pool.apply_async(task, callback=return_callback)
    pool.close()
    pool.join()
