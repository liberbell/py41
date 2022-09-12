from distutils.log import debug
from doctest import master
import logging
from os import rename
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

def worker1(queue):
    # lock.acquire()
    logging.debug("start")
    queue.put(100)
    queue.put(200)
    time.sleep(2)
    # lock.release()
    logging.debug("end")

def worker2(queue):
    # lock.acquire()
    logging.debug("start")
    time.sleep(2)
    print(queue.get())
    print(queue.get())
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
    # d = {"x": 0}
    queue = queue.Queue()
    # semaphore = threading.Semaphore(2)
    t1 = threading.Thread(target=worker1, args=(queue,))
    # t1.setDaemon(True)
    t2 = threading.Thread(target=worker2, args=(queue,))
    # t3 = threading.Thread(target=worker3, args=(semaphore,))
    t1.start()
    t2.start()
    # t3.start()
    # print("started")
    # t1.join()