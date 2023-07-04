# example of asynchronous programming with a process

from time import sleep
from multiprocessing import Process


def task():
    print("Hello from the task", flush=True)
    sleep(1)
    print("The task is all done", flush=True)


if __name__ == "__main__":
    process = Process(target=task)
    process.start()
    print("Main is doing other things...")
    process.join()
