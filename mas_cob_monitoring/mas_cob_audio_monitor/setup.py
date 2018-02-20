#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['mas_cob_audio_monitor'],
   package_dir={'mas_cob_audio_monitor': 'ros/src/mas_cob_audio_monitor'}
)

setup(**d)
