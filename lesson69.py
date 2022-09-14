from multiprocessing import (
    Process, Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Value, Array, Pipe, Manager
)

import logging
import multiprocessing
# import threading
import time

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")

def worker1(i):
    logging.debug("start")
    # logging.debug(i)
    time.sleep(3)
    logging.debug("end")
    return i * 2

def worker2(i):
    logging.debug("start")
    logging.debug(i)
    logging.debug("end")

if __name__ == "__main__":
    # i = 10
    with multiprocessing.Pool(3) as p:
        r = p.map_async(worker1, [100, 200])
        logging.debug("executing")
        logging.debug(r.get())
        # p1 = p.apply_async(worker1, (100, ))
        # p2 = p.apply_async(worker1, (200, ))
        # logging.debug("executing")
        # logging.debug(p1.get())
        # logging.debug(p2.get())

    
    # t1 = multiprocessing.Process(target=worker1, args=(i, ))
    # t1.daemon = True
    # t2 = multiprocessing.Process(name="renaem worker2", target=worker2, args=(i, ))
    # t1.start()
    # t2.start()
    # t2.join()
    # t1.join()