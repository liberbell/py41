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