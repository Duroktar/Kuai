from collections import namedtuple, defaultdict
import threading
import queue
from atexit import register

from kuai.backends import WeakCallback, Singleton, singleton_object


@singleton_object
class ThreadedBackend(metaclass=Singleton):
    handlers = defaultdict(set)
    events = queue.Queue()
    isRunning = False

    def startThread(self):
        self.__thread = threading.Thread(target=self.__engine)
        self.__thread.daemon = True
        self.__thread.start()
        register(self.__stop)

    def addHandler(self, event, callback, *args, **kwargs):
        if not self.isRunning:
            self.isRunning = True
            self.startThread()
        self.handlers[event].add(WeakCallback(callback))

    def handleEvent(self, event, *args, **kwargs):
        if not self.isRunning:
            self.isRunning = True
            self.startThread()
        Event = namedtuple("Event", "name args kwargs")
        self.events.put(Event(event, args, kwargs))

    def __stop(self):
        self.isRunning = False
        self.__thread.join()

    def __engine(self):
        while self.isRunning:
            try:
                currentEvent = self.events.get(timeout=0.3)
            except queue.Empty:
                pass
            else:
                callbacks = self.handlers.get(currentEvent.name)
                if callbacks is not None:
                    for callback in list(callbacks):
                        try:
                            callback(*currentEvent.args, **currentEvent.kwargs)
                        except Exception as e:
                            print("Kuai Exception in `threaded` backend : ", e)
                            raise
                self.events.task_done()


def setup(app):
    app.register_backend('threaded', ThreadedBackend)
