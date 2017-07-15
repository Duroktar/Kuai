Kuài
====

*/Ku·ài/* Fast, swift, swiftness, sharp, to be satisfied, quick, rapid,
rapidness, to hurry up..

.. image:: https://img.shields.io/pypi/v/kuai.svg
    :target: https://pypi.python.org/pypi/kuai

.. image:: https://img.shields.io/travis/Duroktar/Kuai.svg?label=TravisCI
    :target: https://travis-ci.org/Duroktar/Kuai

.. image:: https://img.shields.io/circleci/project/github/RedSparr0w/node-csgo-parser.svg?label=CircleCI
    :target: https://circleci.com/gh/Duroktar/Kuai

.. image:: https://api.codacy.com/project/badge/Grade/7f5e7013a7a34c09bbdae2efc78cdfb6
    :target: https://www.codacy.com/app/Duroktar/Kuai?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Duroktar/Kuai&amp;

.. image:: https://img.shields.io/badge/Donate-Ko--fi-orange.svg
    :target: http://ko-fi.com/A5034CT

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


Contributors
------------

Thank you to anyone who has helped contribute to Kuai in one form or another. If you submit any PR's don't forget to add your name to the list!

xmonader - PR #2 Cleaned up handler definition


Author
------

Scott Doucet / Duroktar / traBpUkciP
