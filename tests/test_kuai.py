from kuai import Kuai, set_backend, kuai_backend
from kuai.backends import Manager


def test_backend():
    set_backend('simple')
    assert kuai_backend() == 'simple'


def test_kuai_singleton():
    a = Kuai()
    b = Kuai()
    c = Kuai()
    assert (a == b == c)


def test_backend_singleton():
    a = Manager()
    b = Manager()
    c = Manager()
    assert (a == b == c)
