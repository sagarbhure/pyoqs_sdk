#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------
# Created By  : Sagar BHURE
# Created Date: 21/11/2021
# version ='1.0'
# --------------------------------------------------------------------

from setuptools import find_packages

from distutils.core import setup

setup(
    name='f5oqs_sdk',
    version='0.4.0',
    author='Quantum Cryptography and beyond',
    author_email='sagarbhureaerospace@gmail.com',
    packages=find_packages(exclude=('tests', 'docs', 'examples')),
    scripts=[],
    url='https://github.com/sagarbhure/f5oqs_sdk',
    license='LICENSE.txt',
    description='Python wrapper for liboqs PyPi package, developed towards hackathon',
    long_description=open('README.md').read(),
)
