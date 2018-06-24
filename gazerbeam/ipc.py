import multiprocessing
import queue # NOTE: Only available in Python3


class Queue(object):
    queue = multiprocessing.Queue()

    @staticmethod
    def send(obj):
        try:
            Queue.queue.put_nowait(obj)
            name = multiprocessing.current_process().name
            print("%s: Sent object %s" % (name, obj))
        except queue.Full:
            pass

    @staticmethod
    def receive():
        try:
            return Queue.queue.get_nowait()
        except queue.Empty:
            pass
