About
-----

.. image:: https://coveralls.io/repos/github/ColinDuquesnoy/QCrash/badge.svg?branch=master
  :target: https://coveralls.io/github/ColinDuquesnoy/QCrash?branch=master
  :alt: API Coverage


.. image:: https://travis-ci.org/ColinDuquesnoy/QCrash.svg?branch=master
   :target: https://travis-ci.org/ColinDuquesnoy/QCrash
   :alt: Travis-CI Build Status


A PyQt/PySide framework for reporting application crash (unhandled exception)
and/or let the user report an issue/feature request.


Features:
---------

- multiple builtin backends for reporting bugs:

  - github_backend: let you create issues on github
  - email_backend: let you send an email with the crash report.

- highly configurable, you can create your own backend, set your own formatter,...
- a thread safe exception hook mechanism with a way to setup your own function

LICENSE
-------

QCrash is licensed under the MIT license.

Installation
------------

``pip install qcrash``

Usage
-----

Basic usage:

.. code-block:: python

    import qcrash.api as qcrash

    # setup our own function to collect system info and application log
    qcrash.get_application_log = my_app.get_application_log
    qcrash.get_system_information = my_app.get_system_info

    # configure backends
    github = qcrash.backends.GithubBackend('ColinDuquesnoy', 'QCrash')
    email = qcrash.backends.EmailBackend('colin.duquesnoy@gmail.com')
    qcrash.install_backend([github, email])

    # install exception hook
    qcrash.install_except_hook()

    # or show the report dialog manually
    qcrash.show_report_dialog()

Some more detailed `examples`_  are available. Also have a look at the
`API documentation`_.

Dependencies
------------

- `keyring`_
- `githubpy`_ (embedded into the package)


.. _keyring: https://pypi.python.org/pypi/keyring
.. _githubpy: https://github.com/michaelliao/githubpy
.. _examples: https://github.com/ColinDuquesnoy/QCrash/tree/master/examples
.. _API documentation: http://qcrash.readthedocs.org/en/latest/index.html


Testing
-------

To run the tests, just run the following command::

    python setup.py test
