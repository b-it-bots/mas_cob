#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['mdr_cob_simple_place'],
   package_dir={'mdr_cob_simple_place': 'ros/src/mdr_cob_simple_place'}
)

setup(**d)
