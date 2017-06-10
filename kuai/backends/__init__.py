import os
from functools import partial

from pluginbase import PluginBase

from kuai.helpers import WeakCallback, Singleton, singleton_object

here = os.path.abspath(os.path.dirname(__file__))
get_path = partial(os.path.join, here)


plugin_base = PluginBase(package='kuai.plugins')
# ------------------------------------

__all__ = [
    'Manager', 'set_backend', 'which_backend',
    'WeakCallback', 'Singleton', 'singleton_object'
]


@singleton_object
class Manager(metaclass=Singleton):
    _backends = {}
    current_backend = None

    def __init__(self):
        self._source = plugin_base.make_plugin_source(
            searchpath=[here]
        )
        self.set_backend()

    @property
    def backend(self):
        return self._backend

    def list_backends(self):
        return self._source.list_plugins()

    def _load_backend(self, name):
        backend = self._source.load_plugin(name)
        backend.setup(self)

    def register_backend(self, name, backend):
        self._backends[name] = backend

    def set_backend(self, name='simple'):
        try:
            self._load_backend(name)
        except Exception as e:
            print(e)
            print("Kuai: {} didn't work.. See error above. "
                  "Please select from,\n".format(name))
            for each in self._source.list_plugins():
                print(" - ", each)
            exit(1)
        else:
            self.current_backend = name
            self._backend = self._backends[name]


def set_backend(name):
    Manager.set_backend(name)


def which_backend():
    print("Backend:", Manager.backend.name)

