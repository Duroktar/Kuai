from collections import namedtuple, defaultdict

from kuai.backends import WeakCallback, Singleton, singleton_object


@singleton_object
class PriorityBackend(metaclass=Singleton):
    handlers = defaultdict(list)

    def addHandler(self, event, callback, priority=5):
        PriorityEvent = namedtuple("PriorityEvent", "priority callback")
        self.handlers[event].append(PriorityEvent(priority, WeakCallback(callback)))

    def handleEvent(self, event, *args, **kwargs):
        handlers = self.handlers.get(event)
        if handlers is None:
            return
        else:
            for handler in sorted(handlers, key=lambda t: t.priority):
                handler.callback(*args, **kwargs)


def setup(app):
    app.register_backend('priority', PriorityBackend)
