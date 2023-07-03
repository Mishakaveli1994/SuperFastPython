# example of a one-off asynchronous task with a process pool executor
from time import sleep
from concurrent.futures import ProcessPoolExecutor


def task():
    print("Hello from the task", flush=True)
    sleep(1)
    print("The task is all done", flush=True)


if __name__ == "__main__":
    with ProcessPoolExecutor() as exe:
        future = exe.submit(task)
        print("Main is doing other things...")
        _ = future.result()
