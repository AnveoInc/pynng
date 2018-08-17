# This software is supplied under the terms of the MIT License, a
# copy of which should be located in the distribution where this
# file was obtained (LICENSE.txt).  A copy of the license may also be
# found online at https://opensource.org/licenses/MIT.

from _nng import ffi, lib

import sys

class Pub(object):
    """
    nng pub0 interface

    .. seealso:: `nng <https://github.com/nanomsg/nng.git>`_
    """
    def __init__(self):
        '''Create Pub socket.'''
        self.sock = ffi.new('nng_socket *')
        self.status = 0

    def open(self):
        '''int nng_pub0_open(nng_socket *s);'''
        self.status = lib.nng_pub0_open(self.sock)

    def listen(self, url):
        '''int nng_listen(nng_socket s, const char *url, nng_listener *lp, int flags);'''
        addr = ffi.new('char[]', url.encode())
        self.status = lib.nng_listen(self.sock[0], addr, ffi.NULL, 0)

    def send(self, data):
        '''int nng_send(nng_socket s, void *data, size_t size, int flags);'''
        buf = ffi.new('char[]', data.encode())
        self.status = lib.nng_send(self.sock[0], buf, len(buf), 0)

    def close(self):
        '''int nng_close(nng_socket s);'''
        self.status = lib.nng_close(self.sock[0])

    def check(self):
        '''Check error code'''
        if self.status != 0:
            print('Code: {}'.format(self.status))


    
