from distutils.log import debug
from doctest import master
import logging
from os import rename
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

def worker1():
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")

def worker2():
    logging.debug("start")
    time.sleep(2)
    logging.debug("end")

if __name__ == "__main__":
    threads = []
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon()
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    # t1 = threading.Thread(target=worker1)
    # t1.setDaemon(True)
    # t2 = threading.Thread(target=worker2)
    # t1.start()
    # t2.start()
    # print("started")
    # t1.join()