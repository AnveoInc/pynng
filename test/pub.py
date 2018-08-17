
# This software is supplied under the terms of the MIT License, a
# copy of which should be located in the distribution where this
# file was obtained (LICENSE.txt).  A copy of the license may also be
# found online at https://opensource.org/licenses/MIT.

import pynng.pub

if __name__ == '__main__':
    pub = pynng.pub.Pub()
    pub.open()
    pub.listen('tcp://127.0.0.1:1337')
    print('Publish message to subscriber (use quit to exit)')
    while True:
        line = input('message> ')
        pub.send(line)
        if line == 'quit':
            break
    pub.close()

    