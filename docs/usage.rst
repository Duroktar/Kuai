=====
Usage
=====

To use Kuai in a project::

    from kuai import Kuai

    def hello(world):
        print("Hello, {world}!".format(world=world))

    Kuai.on('hello-world', hello)

    Kuai.emit('hello-world', 'Kuài')


**TODO**

This section needs more documentation, examples, etc..
