import threading

def worker1():
    print(threading.currentThread().getName(), "start")
    print(threading.currentThread().getName(), "end")