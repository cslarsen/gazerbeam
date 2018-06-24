Gazerbeam
=========

Work in progress; there's nothing here yet.

This project aims to be a realtime, perhaps interactive, visualization of
Python program flow. We'll see how that turns out.

Usage
-----

.. code:: python

    import gazerbeam

    # ...

    @gazerbeam.tracer(another_function)
    def your_function():
        another_function()

The above will intercept all calls to ``another_function``. You can specify any
class, module or a list of them in the argument to ``tracer``.

Installation
------------

.. code:: bash

    $ python3 setup.py install [--user]

Author and license
------------------

Copyright 2018 Christian Stigen Larsen  
Distributed under the LGPL v3 or later.
