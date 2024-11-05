"""Setup file for a ROS 2 package."""

import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'diff_drive'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('config/*')),
        (os.path.join('share', package_name, 'launch'), glob('urdf/*')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'launch'), glob('worlds/*')),
        (os.path.join('share', package_name, 'launch'), glob('models/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Zhengxiao Han',
    maintainer_email='hanzx@u.northwestern.edu',
    description='This package contains a differential drive robot simulation.',
    license='WTFPL',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
