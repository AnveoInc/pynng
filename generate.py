
# This software is supplied under the terms of the MIT License, a
# copy of which should be located in the distribution where this
# file was obtained (LICENSE.txt).  A copy of the license may also be
# found online at https://opensource.org/licenses/MIT.

# Import the FFI 
#
import cffi

# Build the module
#
if __name__ == '__main__':

    # Build the FFI
    #
    ffi = cffi.FFI()

    # Build FFI module and write out the constants
    #
    ffi.set_source('pynng._nng', '#include <nng.h>', libraries=['nng'], library_dirs=['nng/lib'], include_dirs=['nng/include/nng/'])

    # Add the code definitions
    #
    ffi.cdef(open('nng.i').read())

    # Compile
    #
    ffi.compile(verbose=True)
