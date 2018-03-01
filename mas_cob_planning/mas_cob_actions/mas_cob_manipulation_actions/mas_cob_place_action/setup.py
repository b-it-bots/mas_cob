#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['mas_cob_place_action'],
   package_dir={'mas_cob_place_action': 'ros/src/mas_cob_place_action'}
)

setup(**d)
