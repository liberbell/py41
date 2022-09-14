import logging
import time
import threading
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format="%{threadName}s: %{messages}s")

def worker1(d, lock):
    with lock:
        i = d["x"]
        time.sleep(2)
        d["x"] = i + 1
    logging.debug(d)