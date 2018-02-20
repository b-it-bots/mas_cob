#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['mas_cob_tactile_grasp', 'mas_cob_tactile_grasp_common'],
    package_dir={'mas_cob_tactile_grasp': 'ros/src/mas_cob_tactile_grasp',
                 'mas_cob_tactile_grasp_common': 'common/src/mas_cob_tactile_grasp_common'}
)

setup(**d)
