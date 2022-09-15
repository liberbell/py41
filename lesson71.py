import logging
import time
import threading
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')

def f(num, arr):
    logging.debug(num)
    num.value += 1.0
    # conn.send(("test"))
    # time.sleep(2)
    # conn.close()

if __name__ == "__main__":
    num = multiprocessing.Value("f", 0.0)
    arr = multiprocessing.Array("i", [1, 2, 3, 4, 5])
    p = multiprocessing.Process(target=f, (num, arr))
    # parent_conn, child_conn = multiprocessing.Pipe()
    # p = multiprocessing.Process(target=f, args=(parent_conn, ))
    # p.start()
    # p.join()
    # logging.debug(child_conn.recv())