from kuai import Kuai, set_backend
from time import sleep

x = 0


def test_kuai_events():
    set_backend('threaded')

    def increment():
        global x
        x += 1

    Kuai.on('test', increment)
    Kuai.emit('test')
    sleep(0.01)
    assert x == 1

    Kuai.emit('test')
    sleep(0.01)
    assert x == 2
