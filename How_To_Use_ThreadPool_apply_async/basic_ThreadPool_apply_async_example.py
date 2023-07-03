# example of issuing a task with apply_async() to the thread pool
from time import sleep
from multiprocessing.pool import ThreadPool


def task():
    print("Task executing")
    sleep(1)
    print(f"Task done")


if __name__ == "__main__":
    pool = ThreadPool()
    pool.apply_async(task)
    pool.close()
    pool.join()
