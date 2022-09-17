from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register("get_queue")

manager = QueueManager(address=("127.0.0.1"), authkey="thisisakey")