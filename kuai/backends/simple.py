import collections
from kuai.backends import WeakCallback, Singleton, singleton_object


@singleton_object
class SimpleBackend(metaclass=Singleton):
    handlers = collections.defaultdict(list)

    def addHandler(self, event, callback, *args, **kw):
        self.handlers[event].append(WeakCallback(callback))

    def handleEvent(self, event, *args, **kwargs):
        for handler in self.handlers.get(event, []):
            handler(*args, **kwargs)


def setup(app):
    app.register_backend('simple', SimpleBackend)
