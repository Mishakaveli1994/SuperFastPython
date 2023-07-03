# Example of running a function in a new process
from time import sleep
from multiprocessing import Process


# a simple task that block for a moment and prints a message
def task():
    sleep(1)
    print(f"This is coming from another process", flush=True)


# entry point of the program
if __name__ == "__main__":
    # define a task to run in a new process
    process = Process(target=task)
    # start the task in a new process
    process.start()
    # display a message
    print("Waiting for the new process to finish")
    # wait for the task to complete
    process.join()
