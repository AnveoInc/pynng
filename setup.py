# This software is supplied under the terms of the MIT License, a
# copy of which should be located in the distribution where this
# file was obtained (LICENSE.txt).  A copy of the license may also be
# found online at https://opensource.org/licenses/MIT.

from setuptools import setup, find_packages

setup(name='pynng',
      version='1.0.0',
      license='MIT',
      url='https://github.com/nanomsg/nng.git',
      author='Mark Stevens',
      author_email='mark.r.stevens@verizon.net',
      description='cffi-based Python bindings for nng',
      packages=find_packages(),
      include_package_data=True
)