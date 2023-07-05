# example of a mutual execution (mutex) lock
from time import sleep
from random import random, randint
from threading import Thread, Lock


def task(lock, identifier, value):
    with lock:
        print(f">thread {identifier} got the lock, sleeping for {value}")
        sleep(value)


lock = Lock()
for i in range(10):
    #Thread(target=task, args=(lock, i, random())).start()
    Thread(target=task, args=(lock, i, randint(0, 5))).start()
