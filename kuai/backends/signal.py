import collections
from functools import partial
from kuai.backends import WeakCallback, Singleton, singleton_object


@singleton_object
class SignalBackend(metaclass=Singleton):
    """Bind a signal to a variable. 

        Added v0.1.1 - Duroktar

        >>> from kuai import Kuai, set_backend
        >>> set_backend('signal')

        >>> def hello(name):
        >>>     print(f"Hello, {name}")

        >>> signal = Kuai.on('signal', hello)
        >>> signal("cymrow")
    
     """
    handlers = collections.defaultdict(list)

    def addHandler(self, event, callback, *args, **kw):
        self.handlers[event].append(WeakCallback(callback))
        return partial(self.handleEvent, event)

    def handleEvent(self, event, *args, **kwargs):
        for handler in self.handlers.get(event, []):
            handler(*args, **kwargs)


def setup(app):
    app.register_backend('signal', SignalBackend)
