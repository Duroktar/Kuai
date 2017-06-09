
Kuai custom backends
~~~~~~~~~~~~~~~~~~~~

The Kuai backend can be extended by inheriting from the `Singleton` metaclass, decorating with `singleton_object`, overloading two methods..

.. code-block:: python

    # Interface for Kuai.on() call
    addHandler(self, event, callback, *args, **kwargs) 

    # Interface for Kuai.emit() call
    handleEvent(self, event, *args, **kwargs)

then finally registering the class in a `setup` function with a name and reference to the backend.

Here's an example taken straight from the `simple` backend implementation..

.. code-block:: python

    import collections
    from kuai.backends import WeakCallback, Singleton, singleton_object


    @singleton_object
    class SimpleBackend(metaclass=Singleton):
        handlers = handlers = collections.defaultdict(list)

        def addHandler(self, event, callback, *args, **kw):
            self.handlers[event].append(WeakCallback(callback))

        def handleEvent(self, event, *args, **kwargs):
            for handler in self.handlers.get(event, []):
                handler(*args, **kwargs)


    # Register your module with pluginbase.
    def setup(app):
        app.register_backend('simple', SimpleBackend)
