#!/usr/bin/env python

import distutils.core
import catkin_pkg.python_setup

d = catkin_pkg.python_setup.generate_distutils_setup(
   packages=['mas_cob_common_states'],
   package_dir={'mas_cob_common_states': 'ros/src/mas_cob_common_states'}
)

distutils.core.setup(**d)
