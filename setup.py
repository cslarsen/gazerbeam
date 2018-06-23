"""
Setup script for Gazerbeam.

This file is part of the Gazerbeam software.
Copyright 2018 Christian Stigen Larsen

Distributed under the GNU Lesser General Public License (LGPL) v3 or later. See
the file LICENSE.txt for the full license text. This software makes use of open
source software.
"""

import os
import runpy

from setuptools import setup

def get_version():
    """Reads current Gazerbeam version from disk."""
    filename = os.path.join(os.path.dirname(__file__), "gazerbeam", "__init__.py")
    var = runpy.run_path(filename)
    return var["__version__"]

_VERSION = get_version()

setup(
    name="gazerbeam",
    version=_VERSION,
    description="Realtime visualization of Python code trace",
    author="Christian Stigen Larsen",
    author_email="csl@csl.name",
    packages=["gazerbeam"],
    package_dir={"gazerbeam": "gazerbeam"},
    include_package_data=True,
    url="https://github.com/cslarsen/gaezrbeam",
    download_url="https://github.com/cslarsen/gaezrbeam/tarball/v%s" % _VERSION,
    license="https://www.gnu.org/licenses/lgpl-3.0.html",
    long_description=open("README.rst").read(),
    zip_safe=True,
    test_suite="tests",
    keywords=["debugging", "visualization", "development"],
    platforms=["unix", "linux", "osx", "cygwin"],
    install_requires=["vispy", "aspectlib"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
