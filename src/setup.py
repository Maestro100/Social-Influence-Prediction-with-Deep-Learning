#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'protobuf',
    'six',
    'numpy',
    'scipy >= 0.19.1',
    'pillow >= 4.1.1',
]

test_requirements = [
    'pytest',
]

setup(
    name='tensorboard_logger',
    version='0.1.0.dev',
    description='Log TensorBoard events without Tensorflow',
    long_description=readme + '\n\n' + history,
    author='Konstantin Lopuhin',
    author_email='kostia.lopuhin@gmail.com',
    url='https://github.com/TeamHG-Memex/tensorboard_logger',
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
