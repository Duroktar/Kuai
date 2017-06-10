from collections import namedtuple, defaultdict
import threading
import queue
from functools import partial

from kuai.backends import WeakCallback, Singleton, singleton_object


class Worker(threading.Thread):
    def __init__(self, events):
        threading.Thread.__init__(self)
        self.events = events
        self.daemon = True
        self.start()

    def run(self):
        while True:
            try:
                event, callbacks = self.events.get(timeout=0.3)
            except queue.Empty:
                pass
            else:
                if callbacks is not None:
                    for callback in list(callbacks):
                        try:
                            callback(*event.args, **event.kwargs)
                        except Exception as e:
                            print("Kuai Exception in `threaded` backend : ", e)
                self.events.task_done()


@singleton_object
class ThreadPoolBackend(metaclass=Singleton):
    handlers = defaultdict(set)
    isRunning = False

    def __init__(self, num_threads=25):
        self.events = queue.Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.events)

    def addHandler(self, event, callback, *args, **kwargs):
        self.handlers[event].add(WeakCallback(callback))
        return partial(self.handleEvent, event)

    def handleEvent(self, event, *args, **kwargs):
        Event = namedtuple("Event", "name args kwargs")
        callbacks = self.handlers.get(event)
        self.events.put((Event(event, args, kwargs), callbacks))


def setup(app):
    app.register_backend('threadpool', ThreadPoolBackend)
