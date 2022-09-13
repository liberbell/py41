from multiprocessing import (
    Process, Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Value, Array, Pipe, Manager
)

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

def worker1(i):
    logging.debug("start")
    logging.debug(i)
    logging.debug("end")

def worker2(i):
    logging.debug("start")
    logging.debug(i)
    logging.debug("end")

if __name__ == "__main__":
    i = 10
    t1 = threading.Thread(target=worker1, args=(i, ))
    t2 = threading.Thread(name="renaem worker2" target=worker2, args=(i, ))