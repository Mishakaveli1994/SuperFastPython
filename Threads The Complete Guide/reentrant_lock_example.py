# example of a reentrant lock
from time import sleep
from random import random, randint
from threading import Thread, RLock


def report(lock, identifier):
    with lock:
        print(f">thread {identifier} done")


def task(lock, identifier, value):
    with lock:
        print(f">thread {identifier} got the lock, sleeping for {value}")
        sleep(value)
        report(lock, identifier)


lock = RLock()
for i in range(10):
    # Thread(target=task, args=(lock, i, random())).start()
    Thread(target=task, args=(lock, i, random())).start()
