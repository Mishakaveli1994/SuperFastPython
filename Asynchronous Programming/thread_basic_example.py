# example of asynchronous programming with a thread

from time import sleep
from threading import Thread


def task():
    print("Hello from the task")
    sleep(1)
    print("The task is all done")


if __name__ == "__main__":
    thread = Thread(target=task)
    thread.start()
    print("Main is doing other things...")
    thread.join()
