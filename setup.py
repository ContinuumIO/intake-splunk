#!/usr/bin/env python

from setuptools import setup, find_packages
version = '0.0.1'


requires = open('requirements.txt').read().strip().split('\n')

setup(
    name='intake-splunk',
    version=version,
    description='Splunk plugin for Intake',
    url='https://github.com/ContinuumIO/intake-splunk',
    maintainer='Martin Durant',
    maintainer_email='mdurant@anaconda.com',
    license='BSD',
    py_modules=['intake_splunk'],
    packages=find_packages(),
    package_data={'': ['*.csv', '*.yml', '*.html']},
    include_package_data=True,
    install_requires=requires,
    long_description=open('README.rst').read(),
    zip_safe=False,
)
