from ast import main
import logging
import time
import threading
import multiprocessing
from tkinter.tix import MAIN
from turtle import mainloop

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')

def f(conn):
    conn.send(("test"))
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()