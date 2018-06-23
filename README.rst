Gazerbeam
=========

Work in progress; there's nothing here yet.

This project aims to be a realtime, perhaps interactive, visualization of
Python program flow. We'll see how that turns out.

Usage
-----

    import gazerbeam

    # ...

    def your_function():
        with gazerbeam.trace(what=(mymod1, mymod2)):
            another_function()

Installation
------------

    $ python3 setup.py install [--user]

Author and license
------------------

Copyright 2018 Christian Stigen Larsen  
Distributed under the LGPL v3 or later.
