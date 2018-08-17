

# This software is supplied under the terms of the MIT License, a
# copy of which should be located in the distribution where this
# file was obtained (LICENSE.txt).  A copy of the license may also be
# found online at https://opensource.org/licenses/MIT.

from _nng import ffi, lib

import sys

import constants

class Sub(object):
    """
    nng Sub0 interface

    .. seealso:: `nng <https://github.com/nanomsg/nng.git>`_
    """
    def __init__(self):
        '''Create Sub socket.'''
        self.sock = ffi.new('nng_socket *')

    def open(self):
        '''int nng_sub0_open(nng_socket *s);'''
        self.status = lib.nng_sub0_open(self.sock)

    def subscribe(self, topic):
        '''int nng_setopt(nng_socket s, const char *opt, const void *val, size_t valsz);'''
        opt = ffi.new('char[]', constants.NNG_OPT_SUB_SUBSCRIBE.encode())
        val = ffi.new('char[]', topic.encode())
        self.status = lib.nng_setopt(self.sock[0], opt, val, 0)

    def dial(self, url):
        '''int nng_dial(nng_socket s, const char *url, nng_dialer *dp, int flags);'''
        addr = ffi.new('char[]', url.encode())
        self.status = lib.nng_dial(self.sock[0], addr, ffi.NULL, 0)

    def recv(self):
        '''int nng_recv(nng_socket s, void *data, size_t *sizep, int flags);'''
        data = ffi.new('char **')
        sizep = ffi.new('size_t *')
        self.status = lib.nng_recv(self.sock[0], data, sizep, 1)
        message = ffi.string(data[0]).decode("utf-8") 
        lib.nng_free(data[0], sizep[0])
        return message

    def close(self):
        '''int nng_close(nng_socket s);'''
        self.status = lib.nng_close(self.sock[0])

    def check(self):
        '''Check error code'''
        if self.status != 0:
            print('Code: {}'.format(self.status))
