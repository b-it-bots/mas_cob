#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['mdr_cob_tray_actions'],
   package_dir={'mdr_cob_tray_actions': 'ros/src/mdr_cob_tray_actions'}
)

setup(**d)
