# example of wait/notify with a condition
from time import sleep
from threading import Thread, Condition


def task(condition: Condition, work_list: list):
    sleep(3)
    work_list.append(33)
    print("Tread sending notification...")
    with condition:
        condition.notify()


condition = Condition()
work_list = []
print("Main thread waiting for data...")
with condition:
    worker = Thread(target=task, args=(condition, work_list))
    worker.start()
    condition.wait()
print(f"Got data: {work_list}")
