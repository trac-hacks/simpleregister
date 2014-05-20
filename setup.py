#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='SimpleRegister', version='0.1',
    packages=find_packages(),
    entry_points = {
        'trac.plugins': [
            'simpleregister = simpleregister.simpleregister',
        ],
    },
	package_data = {'simpleregister': ['templates/*',]},
)
