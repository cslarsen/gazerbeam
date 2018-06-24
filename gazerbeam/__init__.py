#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Realtime visualization of Python code trace.

This file is part of the Gazerbeam software.
Copyright 2018 Christian Stigen Larsen

Distributed under the GNU Lesser General Public License (LGPL) v3 or later. See
the file LICENSE.txt for the full license text. This software makes use of open
source software.
"""

__author__ = "Christian Stigen Larsen"
__copyright__ = "Copyright 2018 Christian Stigen Larsen"
__license__ = "GNU LGPL v3 or later"
__version__ = "0.0.1"

from gazerbeam.logger import Logger
from gazerbeam.tracer import tracer
import gazerbeam.process
import gazerbeam.ipc

stamp = Logger.stamp

def start_viewer():
    gazerbeam.process.Process.start()

def stop_viewer():
    gazerbeam.ipc.Queue.send("STOP")
    gazerbeam.process.Process.join()

__all__ = [
    "close_viewer",
    "stamp",
    "start_viewer",
    "tracer",
]
