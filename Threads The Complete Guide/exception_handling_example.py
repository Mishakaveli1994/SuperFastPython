# example of an unhandled exception in a thread
import threading
from time import sleep
from threading import Thread


def custom_hook(args):
    print(f"Thread failed: {args.exc_value}")


def work():
    print("Working...")
    sleep(1)
    raise Exception("Something bad happened")


threading.excepthook = custom_hook
thread = Thread(target=work)
thread.start()
thread.join()
print("Continuing on...")
print("Doing stuff after exception")
