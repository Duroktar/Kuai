====
Kuài
====

*/Ku·ài/* Fast, swift, swiftness, sharp, to be satisfied, 
quick, rapid, rapidness, to hurry up..

.. image:: https://img.shields.io/pypi/v/kuai.svg
        :target: https://pypi.python.org/pypi/kuai

.. image:: https://img.shields.io/travis/Duroktar/kuai.svg
        :target: https://travis-ci.org/Duroktar/kuai

.. image:: https://readthedocs.org/projects/kuai/badge/?version=latest
        :target: https://kuai.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/Duroktar/kuai/shield.svg
     :target: https://pyup.io/repos/github/Duroktar/kuai/
     :alt: Updates


Simple & fast event library.


* Free software: MIT license
* Documentation: https://kuai.readthedocs.io.


Install
-------

*Not on pip yet, install dev mode*


Develop
-------

.. code-block:: bash

    clone https://github.com/Duroktar/Kuai.git
    cd Kuai
    pip install -e .


Kuài is Fast
------------

Save in a hello.py:

.. code-block:: python

    from kuai import Kuai

    def hello(world):
        print(f"Hello, {world}!")

    Kuai.on('hello-world', hello)
    Kuai.emit('hello-world', 'Kuài')

It's as easy as

.. code-block:: bash

    $ pip install Kuai
    $ python hello.py
     Hello, Kuài!


.. include:: ./CONTRIBUTING.rst


License
-------

MIT


Author
------

Scott Doucet / Duroktar / traBpUkciP


Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

