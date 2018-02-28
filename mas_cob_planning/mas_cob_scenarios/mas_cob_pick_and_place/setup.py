#!/usr/bin/env python

import distutils.core
import catkin_pkg.python_setup

d = catkin_pkg.python_setup.generate_distutils_setup(
   packages=['mas_cob_pick_and_place'],
   package_dir={'mas_cob_pick_and_place': 'ros/src/mas_cob_pick_and_place'}
)

distutils.core.setup(**d)
