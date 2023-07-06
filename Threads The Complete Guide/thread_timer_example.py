# example of using a thread timer object
from threading import Timer


def task(message):
    print(message)


timer = Timer(3, task, args=("Hello world",))
timer.start()
print(f"Waiting for the time...")
