====
Kuài
====

.. image:: https://github.com/Duroktar/Kuai/blob/master/assets/Kuai-logo.png?raw=true
   :scale: 80 %
   :alt: /Ku·ài/
   :align: right

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


* Documentation: https://kuai.readthedocs.io
* Free software: MIT license


**Kuài is Fast**

Save in a hello.py:

.. code-block:: python

    from kuai import Kuai

    def hello(world):
        print(f"Hello, {world}!")

    Kuai.on('hello-world', hello)
    Kuai.emit('hello-world', 'Kuài')


**Kuài is Easy**

.. code-block:: bash

    $ pip install Kuai
    $ python hello.py
    Hello, Kuài!

**Kuài is Cool**

.. code-block:: python

    from kuai import Kuài

    Kuài.emit('~%& Kuài &%~')
