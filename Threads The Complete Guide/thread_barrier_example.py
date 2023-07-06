# example of using a barrier
from time import sleep
from random import random
from threading import Thread, Barrier


def task(barrier: Barrier, number):
    value = random() * 10
    sleep(value)
    print(f"Thread {number} done, got: {value}")
    barrier.wait()


# +1 for the main thread
barrier = Barrier(5 + 1)
for i in range(4):
    worker = Thread(target=task, args=(barrier, i))
    worker.start()

print("Main tread waiting on all results...")
barrier.wait()
print("All threads have their result")
