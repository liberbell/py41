from multiprocessing.managers import BaseManager
import queue

class QueueManager(BaseManager):
    pass

QueueManager.register("get_queue")

manager = QueueManager(address=("127.0.0.1", 50000), authkey=b"thisisakey")
manager.connect()
queue = manager.get_queue()
queue.put("hello")