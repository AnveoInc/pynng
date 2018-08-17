
# This software is supplied under the terms of the MIT License, a
# copy of which should be located in the distribution where this
# file was obtained (LICENSE.txt).  A copy of the license may also be
# found online at https://opensource.org/licenses/MIT.

import pynng.sub

if __name__ == '__main__':
    sub = pynng.sub.Sub()
    sub.open()
    sub.dial('tcp://127.0.0.1:1337')
    sub.subscribe('')
    print('Receive messages from publisher')
    while True:
        line = str(sub.recv())
        print('recv> {}'.format(line))
        if line == 'quit':
            break
    sub.close()
