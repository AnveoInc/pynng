#!/bin/sh

# This software is supplied under the terms of the MIT License, a
# copy of which should be located in the distribution where this
# file was obtained (LICENSE.txt).  A copy of the license may also be
# found online at https://opensource.org/licenses/MIT.

# Download NNG from github
#
function do_fetch() {
    mkdir -p nng
    cd nng
    git clone https://github.com/nanomsg/nng.git source
    cd ..
}

# Build NNG as a static library
#
function do_compile_nng() {
    cd nng
    mkdir -p build
    cd build
    cmake ../source -DCMAKE_INSTALL_PREFIX=.. #-DBUILD_SHARED_LIBS=ON
    make install
    cd ../..
}

# Compile the CFFI interface for PYNNG
#
function do_compile_pynng() {
    cat nng/include/nng/nng.h nng/include/nng/protocol/pubsub0/pub.h nng/include/nng/protocol/pubsub0/sub.h > nng.h
    grep "define NNG_OPT" nng.h | awk '{ print $2 "="  $3 }' > pynng/constants.py
    gcc -nostdinc -E nng.h | grep -v \# > nng.i
    python generate.py
}

# Build the PIP package from the compiled objects
#
function do_install() {
    mv *.so pynng/_pynng.so
    python setup.py sdist
    pip install --upgrade --no-deps --force-reinstall dist/pynng-1.0.0.tar.gz
}

# Clean up all of the intermediate files
#
function do_cleanup() {
    rm -rf nng
    rm -rf pynng/_nng.o 
    rm -rf pynng/_nng.c
    rm -rf pynng/*.so
    rm -rf pynng/constants.py
    rm -rf pynng.egg-info
    rm -rf dist
    rm -rf __pycache__
    rm -rf pynng/__pycache__
    rm -rf nng.h nng.i defines.h
}

# Steps
#
do_fetch
do_compile_nng
do_compile_pynng
do_install
do_cleanup
