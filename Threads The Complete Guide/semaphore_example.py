# example of using a semaphore
from time import sleep
from random import random
from threading import Thread, Semaphore


def task(semaphore: Semaphore, number):
    with semaphore:
        value = random()
        sleep(value)
        print(f"Thread {number} got {value}")


def task_ns(number):
    value = random()
    sleep(value)
    print(f"Thread {number} got {value}")


semaphore = Semaphore(2)
for i in range(10):
    worker = Thread(target=task, args=(semaphore, i))
    # worker = Thread(target=task_ns, args=(i,))
    worker.start()
