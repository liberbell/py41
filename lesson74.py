import threading
import multiprocessing

import concurrent.futures
import logging
import time

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")
logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")