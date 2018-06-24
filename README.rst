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

The above will intercept all calls to ``another_function``. You can also trace
classes, modules, generators and more. If you want to trace more objects, pass
them in a tuple to ``tracer``'s argument.

In time, the effect will be that a window will open with a realtime graphical
trace of all the calls to the specified objects, along with input and output
arguments.

I don't know exactly how much I will be able to implement, but it would be
really nice with slow-motion playback.

Installation
------------

.. code:: bash

    $ python3 setup.py install [--user]

When this project is mature enough, I will upload it to PyPi so that you just
have to type ``pip3 install [--user] gazerbeam`` to install it.

Author and license
------------------

Copyright 2018 Christian Stigen Larsen

Distributed under the LGPL v3 or later.
