# example of issuing a task with apply_async() and waiting for the task to complete
from time import sleep
from random import random
from multiprocessing.pool import ThreadPool


def task():
    print("Task executing")
    sleep(1)
    print(f"Task done")


if __name__ == "__main__":
    pool = ThreadPool()
    result = pool.apply_async(task)
    result.wait()
    pool.close()
