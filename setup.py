#!/bin/env python
from setuptools import setup
from codecs import open
from os import path

here = path.dirname(path.abspath(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PoolPhysics',
    version='0.0.1',
    description='Event-based pool physics simulator',
    packages=['pool_physics'],
    long_description=long_description,
    url='https://github.com/jzitelli/PoolPhysics',
    author='Jeffrey Zitelli',
    author_email='jeffrey.zitelli@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='pool billiards event based physics',
    install_requires=['numpy', 'pillow'],
    extras_require={},
    # package_data={
    # },
    data_files=[],
)
