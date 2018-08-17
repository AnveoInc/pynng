
Start on Python bindings for nng (https://github.com/nanomsg/nng)

The approach was based on https://github.com/nanomsg/nnpy

Run the build.sh script to download, compile NNG, build CFFI shared library, package the library and install using pip. The script cleans up intermediate files, so please examine the build.sh before running.

Currently only tested on Max OS X using Python 3.6.5 :: Anaconda, Inc.. Other platforms and Python versions could be supported if there is interest.

This version is an initial proof of concept and only supports the Pub0/Sub0 protocol. Two test cases are provided.

To run:

1. Open a terminal. prompt> python test/pub.py
2. Open a second terminal. prompt> python/sub.py
