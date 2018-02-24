#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['mas_cob_tactile_tools', 'mas_cob_tactile_tools_common'],
    package_dir={'mas_cob_tactile_tools': 'ros/src/mas_cob_tactile_tools',
                 'mas_cob_tactile_tools_common': 'common/src/mas_cob_tactile_tools_common'}
)

setup(**d)
