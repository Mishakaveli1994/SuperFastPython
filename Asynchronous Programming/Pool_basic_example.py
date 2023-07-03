# example of a one-off asynchronous task with a pool
from time import sleep
from multiprocessing.pool import Pool


def task():
    print("Hello from the task")
    sleep(1)
    print("Task is all done")


if __name__ == "__main__":
    with Pool() as pool:
        async_result = pool.apply_async(task)
        print(f"Main is doing other things...")
        async_result.wait()
