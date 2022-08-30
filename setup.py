#!/usr/bin/env python

from setuptools import setup, find_packages

import djangosphinx

setup(
    name='djangosphinx',
    version=".".join(map(str, djangosphinx.__version__)),
    author='Igor',
    author_email='igor@gmail.com',
    url='http://github.com/igor-oshn/django-sphinx',
    install_requires=['django'],
    description = 'An integration layer bringing Django and Sphinx Search together.',
    packages=find_packages('raros'),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
