

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Custom backend
~~~~~~~~~~~~~~

The Kuai backend can be extended by inheriting from the `Singleton` metaclass, decorating with `singleton_object`, overloading two methods..

.. code-block:: python

    # Interface for Kuai.on() call
    addHandler(self, event, callback, *args, **kwargs) 

    # Interface for Kuai.emit() call
    handleEvent(self, event, *args, **kwargs)

then finally registering the class in a `setup` function with a name and reference to the backend.

Here's an example taken straight from the `simple` backend implementation..

.. code-block:: python

    import collections
    from kuai.backends import WeakCallback, Singleton, singleton_object


    @singleton_object
    class SimpleBackend(metaclass=Singleton):
        handlers = handlers = collections.defaultdict(list)

        def addHandler(self, event, callback, *args, **kw):
            self.handlers[event].append(WeakCallback(callback))

        def handleEvent(self, event, *args, **kwargs):
            for handler in self.handlers.get(event, []):
                handler(*args, **kwargs)


    # Register your module with pluginbase.
    def setup(app):
        app.register_backend('simple', SimpleBackend)


Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/Duroktar/kuai/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Kuai could always use more documentation, whether as part of the
official Kuai docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/Duroktar/kuai/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)


Get Started!
------------

.. highlight:: shell

Ready to contribute? Here's how to set up `kuai` for local development.

1. Fork the `kuai` repo on GitHub.
2. Clone your fork locally::

    $ git clone https://github.com/Duroktar/kuai.git

3. Install your local copy into a virtualenv. This is how I set up my workspace for local development::

    $ python -m venv env
    $ cd kuai/
    $ pip install --upgrade pip
    $ pip install -e .
    $ pip install -r requirements_dev.txt

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-feature-or-backend

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass the tests, including both Python 3.5 and 3.6::

    $ tox

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature-or-backend

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.5 and up. Check
   https://travis-ci.org/Duroktar/kuai/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ py.test tests.test_kuai

