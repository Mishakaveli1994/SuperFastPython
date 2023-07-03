# example of a one-time asynchronous task with a thread pool executor
from time import sleep
from concurrent.futures import ThreadPoolExecutor


def task():
    print("Hello from the task", flush=True)
    sleep(1)
    print("Task is all done")
    return "The task is completed"


if __name__ == "__main__":
    with ThreadPoolExecutor() as exe:
        future = exe.submit(task)
        print("Main is doing other things...")
        print(future.result())
