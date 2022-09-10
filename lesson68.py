from distutils.log import debug
from doctest import master
import logging
from os import rename
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

def worker1():
    logging.debug("start")
    # print(threading.currentThread().getName(), "start")
    time.sleep(0.5)
    logging.debug("end")
    # print(threading.currentThread().getName(), "end")

def worker2():
    logging.debug("start")
    # print(threading.currentThread().getName(), "start")
    time.sleep(0.5)
    logging.debug("end")
    # print(threading.currentThread().getName(), "end")

if __name__ == "__main__":
    t1 = threading.Thread(name="rename worker1", target=worker1)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print("started")