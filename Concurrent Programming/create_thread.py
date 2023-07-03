# example of executing a target task function in a separate thread
from time import sleep
from threading import Thread


# a simple task that blocks for a moment and printas a message
def task():
    sleep(1)
    print("This is coming from another thread.")


thread = Thread(target=task)
thread.start()
print("Waiting for the new thread to finish")
thread.join()
