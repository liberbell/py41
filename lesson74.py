import threading
import multiprocessing

import concurrent.futures
import logging
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")

def worker(x, y):
    logging.debug("start")
    r = x * y
    logging.debug(r)
    logging.debug("end")

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        f1 = executor.submit(worker, 2, 5)

if __name__ == "__main__":
    main()