# example of a one-time asynchronous task with a thread pool executor wtih submit
# Get result and raise timeout error if it takes too long
from time import sleep
from concurrent.futures import ThreadPoolExecutor, TimeoutError


def task():
    sleep(1)
    return "The task is completed"


if __name__ == "__main__":
    with ThreadPoolExecutor() as exe:
        future = exe.submit(task)
        try:
            print("Main is doing other things...")
            print(future.result(timeout=0.5))
        except TimeoutError:
            print("Waited too long for result")
