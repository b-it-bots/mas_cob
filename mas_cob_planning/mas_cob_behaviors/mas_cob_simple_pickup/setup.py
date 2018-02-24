#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['mas_cob_simple_pickup'],
   package_dir={'mas_cob_simple_pickup': 'ros/src/mas_cob_simple_pickup'}
)

setup(**d)
