#!/usr/bin/env python3

import re
from setuptools import setup


with open('./tinder_token/__init__.py') as f:
    version = re.search(r'(?<=__version__ = .)([\d\.]*)', f.read()).group(1)


if __name__ == '__main__':
    setup(
        name='tinder-token',
        version=version,
        author='Zsolt Mester',
        author_email='',
        url='https://github.com/meister245/tinder-token',
        packages=[
            'tinder_token'
        ],
        install_requires=[
            'requests'
        ],
        extras_require={
            'facebook': ['robobrowser', 'html5lib', 'Werkzeug==0.16.1']
        },
        include_package_data=True,
        scripts=[
            'scripts/tinder-token.py'
        ],
        license='MIT'
    )
