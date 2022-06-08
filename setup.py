#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(join(dirname(__file__), *names), encoding=kwargs.get('encoding', 'utf8')) as fh:
        return fh.read()


setup(
    name='binance_utils',
    version='0.0.1',
    description='',
    author='Jonathan Els',
    author_email='jonathanelscpt@gmail.io',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.8',
    install_requires=[
        'python-binance',
        'typer',
        'tabulate',
        'Pygments'
    ],
    entry_points={
        'console_scripts': [
            'binance-utils = binance_utils.cli:main',
        ]
    },
)
