Kuài
====

*/Ku·ài/* Fast, swift, swiftness, sharp, to be satisfied, quick, rapid,
rapidness, to hurry up..

.. image:: https://img.shields.io/pypi/v/kuai.svg
    :target: https://pypi.python.org/pypi/kuai

.. image:: https://img.shields.io/travis/Duroktar/kuai.svg
    :target: https://travis-ci.org/Duroktar/kuai

Simple & fast event library.

-  Free software: MIT license
-  Documentation: http://pythonhosted.org/Kuai/


Install
-------

.. code-block:: bash

    $ pip install Kuai --user


Develop
-------

.. code-block:: bash

    $ clone https://github.com/Duroktar/Kuai.git
    $ cd Kuai
    $ pip install -e .


Kuai is Fast
------------

Save in a hello.py:

.. code-block:: python

    from kuai import Kuai

    def hello(world):
        print(f"Hello, {world}!")

    Kuai.on('hello-world', hello)
    Kuai.emit('hello-world', 'Kuài')

It’s as easy as

.. code-block:: bash

    $ pip install Kuai
    $ python hello.py
     Hello, Kuài!


License
-------

MIT


Author
------

Scott Doucet / Duroktar / traBpUkciP


Contributors
------------

Thank you to anyone who has helped contribute to Kuai in one form or another. If you submit any PR's don't forget to add your name to the list!

xmonader - PR #2 Cleaned up handler definition
