from kuai import Kuai, set_backend

x = 0


def test_kuai_events():
    set_backend('simple')

    def increment():
        global x
        x += 1

    Kuai.on('test', increment)
    Kuai.emit('test')
    assert x == 1

    Kuai.emit('test')
    assert x == 2
