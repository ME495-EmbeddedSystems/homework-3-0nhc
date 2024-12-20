"""Setup file for a ROS 2 package."""

from glob import glob

import os

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
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
        (os.path.join(
            'share',
            package_name, 'env-hooks'),
            glob('env-hooks/*')),
        (os.path.join(
            'share',
            package_name,
            'models/asphalt_plane/materials/scripts'),
            glob('models/asphalt_plane/materials/scripts/*.material')),
        (os.path.join(
            'share',
            package_name,
            'models/cardboard_box/materials/scripts'),
            glob('models/cardboard_box/materials/scripts/*.material')),
        (os.path.join(
            'share',
            package_name,
            'models/jersey_barrier/materials/scripts'),
            glob('models/jersey_barrier/materials/scripts/*.material')),
        (os.path.join(
            'share',
            package_name,
            'models/asphalt_plane/materials/textures'),
            glob('models/asphalt_plane/materials/textures/*')),
        (os.path.join(
            'share',
            package_name,
            'models/cardboard_box/materials/textures'),
            glob('models/cardboard_box/materials/textures/*')),
        (os.path.join(
            'share',
            package_name,
            'models/jersey_barrier/materials/textures'),
            glob('models/jersey_barrier/materials/textures/*')),
        (os.path.join(
            'share',
            package_name,
            'models/asphalt_plane/thumbnails'),
            glob('models/asphalt_plane/thumbnails/*')),
        (os.path.join(
            'share',
            package_name,
            'models/cardboard_box/thumbnails'),
            glob('models/cardboard_box/thumbnails/*')),
        (os.path.join(
            'share',
            package_name,
            'models/jersey_barrier/thumbnails'),
            glob('models/jersey_barrier/thumbnails/*')),
        (os.path.join(
            'share',
            package_name,
            'models/asphalt_plane/meshes'),
            glob('models/asphalt_plane/meshes/*')),
        (os.path.join(
            'share',
            package_name,
            'models/cardboard_box/meshes'),
            glob('models/cardboard_box/meshes/*')),
        (os.path.join(
            'share',
            package_name,
            'models/jersey_barrier/meshes'),
            glob('models/jersey_barrier/meshes/*')),
        (os.path.join(
            'share',
            package_name,
            'models/furina/meshes'),
            glob('models/furina/meshes/*')),
        (os.path.join(
            'share',
            package_name,
            'models/zhongli/meshes'),
            glob('models/zhongli/meshes/*')),
        (os.path.join(
            'share',
            package_name,
            'models/raiden_shogun/meshes'),
            glob('models/raiden_shogun/meshes/*')),
        (os.path.join(
            'share',
            package_name,
            'models/nahida/meshes'),
            glob('models/nahida/meshes/*')),
        (os.path.join(
            'share',
            package_name,
            'models/asphalt_plane'),
            glob('models/asphalt_plane/*.config')),
        (os.path.join(
            'share',
            package_name,
            'models/cardboard_box'),
            glob('models/cardboard_box/*.config')),
        (os.path.join(
            'share',
            package_name,
            'models/jersey_barrier'),
            glob('models/jersey_barrier/*.config')),
        (os.path.join(
            'share',
            package_name,
            'models/furina'),
            glob('models/furina/*.config')),
        (os.path.join(
            'share',
            package_name,
            'models/zhongli'),
            glob('models/zhongli/*.config')),
        (os.path.join(
            'share',
            package_name,
            'models/raiden_shogun'),
            glob('models/raiden_shogun/*.config')),
        (os.path.join(
            'share',
            package_name,
            'models/nahida'),
            glob('models/nahida/*.config')),
        (os.path.join(
            'share',
            package_name,
            'models/asphalt_plane'),
            glob('models/asphalt_plane/*.sdf')),
        (os.path.join(
            'share',
            package_name,
            'models/cardboard_box'),
            glob('models/cardboard_box/*.sdf')),
        (os.path.join(
            'share',
            package_name,
            'models/jersey_barrier'),
            glob('models/jersey_barrier/*.sdf')),
        (os.path.join(
            'share',
            package_name,
            'models/furina'),
            glob('models/furina/*.sdf')),
        (os.path.join(
            'share',
            package_name,
            'models/raiden_shogun'),
            glob('models/raiden_shogun/*.sdf')),
        (os.path.join(
            'share',
            package_name,
            'models/zhongli'),
            glob('models/zhongli/*.sdf')),
        (os.path.join(
            'share',
            package_name,
            'models/nahida'),
            glob('models/nahida/*.sdf')),
        (os.path.join(
            'share',
            package_name,
            'models/asphalt_plane'),
            glob('models/asphalt_plane/*.pbtxt')),
        (os.path.join(
            'share',
            package_name,
            'models/cardboard_box'),
            glob('models/cardboard_box/*.pbtxt')),
        (os.path.join(
            'share',
            package_name,
            'models/jersey_barrier'),
            glob('models/jersey_barrier/*.pbtxt')),
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
            'flip = diff_drive.flip:main',
        ],
    },
)
