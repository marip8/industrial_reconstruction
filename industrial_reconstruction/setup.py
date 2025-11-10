from setuptools import setup
import os
from glob import glob

package_name = 'industrial_reconstruction'

setup(
    name=package_name,
    version='0.1.0',
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.*')),
    ],
    install_requires=[
        'setuptools',
        'launch',
        'launch_ros'
    ],
    zip_safe=True,
    author='Tyler Marr',
    author_email='tyler.marr@swri.org',
    maintainer='Tyler Marr',
    maintainer_email='tyler.marr@swri.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='A ROS2 reconstruction utility leveraging TSDF from Open3D',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    scripts=[
        'scripts/archive_player',
        'scripts/industrial_reconstruction'
    ]
)
