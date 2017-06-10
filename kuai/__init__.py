# -*- coding: utf-8 -*-
from kuai.helpers import Singleton, singleton_object
from kuai.backends import Manager, set_backend

__author__ = """Scott Doucet"""
__email__ = 'duroktar@gmail.com'
__version__ = '0.1.3'
__all__ = [
    'Kuai', 'Kuài', 'KuaiBase',
    'kuai_backend', 'set_backend'
]


@singleton_object
class Kuai(metaclass=Singleton):

    @classmethod
    def on(cls, event, callback, *args, **kwargs):
        return Manager.backend.addHandler(event, callback, *args, **kwargs)

    @classmethod
    def emit(cls, event, *args, **kwargs):
        Manager.backend.handleEvent(event, *args, **kwargs)

    @property
    def which_backend(self):
        return Manager.current_backend


class KuaiBase:
    def on(cls, event, callback, *args, **kwargs):
        Manager.backend.addHandler(event, callback, *args, **kwargs)

    def emit(cls, event, *args, **kwargs):
        Manager.backend.handleEvent(event, *args, **kwargs)


def kuai_backend():
    return str(Kuai.which_backend)


Kuài = Kuai
