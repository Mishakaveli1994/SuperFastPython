# example of issuing a task with apply_async() with args to the thread pool
from time import sleep
from multiprocessing.pool import ThreadPool


def task(message):
    print(f"Task executing: {message}")
    sleep(1)
    print(f"Task done: {message}")


if __name__ == "__main__":
    pool = ThreadPool()
    pool.apply_async(task, args=("Hello, world!",))
    pool.close()
    pool.join()
