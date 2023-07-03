# example of a one-time asynchronous task with a thread pool executor with map
# Get result
from time import sleep
from concurrent.futures import ThreadPoolExecutor


def work(value):
    sleep(1)
    return f"The task is done: {value}"


if __name__ == "__main__":
    with ThreadPoolExecutor() as exe:
        for result in exe.map(work, range(3)):
            print(result)
