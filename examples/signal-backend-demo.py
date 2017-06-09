from kuai import Kuai, set_backend
set_backend('signal')


def hello(name):
    print(f"Hello, {name}")


signal = Kuai.on('signal', hello)
signal("cymrow")
