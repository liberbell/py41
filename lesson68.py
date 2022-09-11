from distutils.log import debug
from doctest import master
import logging
from os import rename
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

def worker1(x, y=1):
    logging.debug("start")
    i = d["x"]
    d["x"] = i + 1
    # time.sleep(2)
    logging.debug(d)
    logging.debug("end")

def worker2(d):
    logging.debug("start")
    i = d["x"]
    d["x"] = i + 1
    # time.sleep(2)
    logging.debug(d)
    logging.debug("end")

if __name__ == "__main__":
    # t = threading.Timer(3, worker1, args=(100,), kwargs={"y": 200})
    # t.start()
    # threads = []
    # for _ in range(5):
    #     t = threading.Thread(target=worker1)
    #     t.setDaemon(True)
    #     t.start()
    # print(threading.enumerate())
    # for thread in threading.enumerate():
    #     if thread is threading.current_thread():
    #         print(thread)
    #         continue
    #     thread.join()
    d = {"x": 0}
    t1 = threading.Thread(target=worker1, args=(d, ))
    # t1.setDaemon(True)
    t2 = threading.Thread(target=worker2, args=(d, ))
    t1.start()
    t2.start()
    # print("started")
    # t1.join()