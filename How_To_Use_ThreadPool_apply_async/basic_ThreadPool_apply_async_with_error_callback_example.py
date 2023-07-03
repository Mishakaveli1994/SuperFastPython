# example of issuing a task with apply_async() with an error callback function to the thread pool
from time import sleep
from random import random
from multiprocessing.pool import ThreadPool


def custom_error_callback(error):
    print(f"Got an error: {error}")


def task():
    value = random()
    print(f"Task generated value {value}")
    sleep(1)
    raise Exception("Ooooh an error")
    print(f"Task done with value {value}")
    return value


if __name__ == "__main__":
    pool = ThreadPool()
    pool.apply_async(task, error_callback=custom_error_callback)
    pool.close()
    pool.join()
