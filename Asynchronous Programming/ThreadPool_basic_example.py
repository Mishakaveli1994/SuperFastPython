# example of a one-off asynchronous task with a thread pool
from time import sleep
from multiprocessing.pool import ThreadPool


def task():
    print("Hello from the task")
    sleep(1)
    print("Task is all done")


if __name__ == "__main__":
    with ThreadPool() as pool:
        async_result = pool.apply_async(task)
        print(f"Main is doing other things...")
        async_result.wait()
