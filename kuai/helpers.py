# -*- coding: utf-8 -*-
"""Various helper functions for Kuai, these are all from stackoverflow. Amen."""
import weakref
import inspect


def singleton_object(cls):
    """Class decorator that transforms (and replaces) a class definition (which
    must have a Singleton metaclass) with the actual singleton object. Ensures
    that the resulting object can still be "instantiated" (i.e., called),
    returning the same object. Also ensures the object can be pickled, is
    hashable, and has the correct string representation (the name of the
    singleton)
    """
    assert isinstance(cls, Singleton), \
        cls.__name__ + " must use Singleton metaclass"

    def self_instantiate(self):
        return self

    cls.__call__ = self_instantiate
    cls.__hash__ = lambda self: hash(cls)
    cls.__repr__ = lambda self: cls.__name__
    cls.__reduce__ = lambda self: cls.__name__
    obj = cls()
    obj.__name__ = cls.__name__
    return obj


class Singleton(type):
    """Metaclass for singleton objects. Any instantiation of a
    Singleton class yields the exact same object, e.g.:

    >>> class MyClass(metaclass=Singleton):
            pass
    >>> a = MyClass()
    >>> b = MyClass()
    >>> a is b
    True
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = \
                super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    @classmethod
    def __instancecheck__(mcs, instance):
        if instance.__class__ is mcs:
            return True
        else:
            return isinstance(instance.__class__, mcs)


class WeakCallback(object):
    """A Weak Callback object that will keep a reference to
    the connecting object with weakref semantics.

    This allows object A to pass a callback method to object S,
    without object S keeping A alive. **Extended to work with
    unbound calls, ie: functions, lambdas..
    """
    def __init__(self, callback):
        """Create a new Weak Callback calling @callback"""
        if inspect.ismethod(callback):
            obj = callback.__self__
            attr = callback.__func__.__name__
        else:
            obj = callback
            attr = None
        self.__wref = weakref.ref(obj, self.__object_deleted)
        self.__callback_attr = attr

    def __hash__(self):
        return hash(self.__wref)

    def __eq__(self, other):
        if not isinstance(other, WeakCallback):
            return False
        return hash(self) == hash(other)

    def __call__(self, *args, **kwargs):
        obj = self.__wref()
        if obj:
            if self.__callback_attr:
                attr = getattr(obj, self.__callback_attr)
            else:
                attr = obj
            attr(*args, **kwargs)
        else:
            self.__default_callback(*args, **kwargs)

    def __default_callback(self, *args, **kwargs):
        """Called instead of callback when expired"""
        pass

    def __object_deleted(self, wref):
        """Called when callback expires"""
        pass
