# example of using an event
from time import sleep
from random import random
from threading import Thread, Event


def task(event, number):
    event.wait()
    value = random()
    sleep(value)
    print(f"Thread {number} got {value}")


event = Event()
for i in range(5):
    thread = Thread(target=task, args=(event, i))
    thread.start()
print("Main thread blocking")
sleep(2)
event.set()
