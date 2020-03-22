#!/usr/bin/env python3

import re
from setuptools import setup


with open('./tinder_token/__init__.py') as f:
    version = re.search(r'(?<=__version__ = .)([\d\.]*)', f.read()).group(1)


with open(r'./requirements.txt', 'r') as f:
    install_requires = [x for x in f.read().split('\n') if len(x) > 0]


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
        install_requires=install_requires,
        include_package_data=True,
        console_scripts=[
            'scripts/tinder-token.py'
        ],
        license='MIT'
    )
