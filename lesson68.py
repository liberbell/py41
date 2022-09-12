from distutils.log import debug
from doctest import master
import logging
from os import rename
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

def worker1():
    logging.debug("start")
    logging.debug("end")

def worker2(queue):
    # lock.acquire()
    logging.debug("start")
    time.sleep(2)
    logging.debug(queue.get())
    logging.debug(queue.get())
    # print(queue.get())
    # lock.release()
    logging.debug("end")

# def worker3(lock):
#     with semaphore:
#         # lock.acquire()
#         logging.debug("start")
#         time.sleep(2)
#         # lock.release()
#         logging.debug("end")

# def worker2(d, lock):
#     logging.debug("start")
#     lock.acquire()
#     i = d["x"]
#     d["x"] = i + 1
#     # time.sleep(2)
#     logging.debug(d)
#     lock.release()
#     logging.debug("end")

if __name__ == "__main__":
    t1 = threading.Thread(target=worker1, args=(queue,))
    t1.start()
