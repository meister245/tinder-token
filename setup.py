#!/usr/bin/env python3

import re
from setuptools import setup


with open('./tinder_token/__init__.py', 'r') as f:
    version = re.search(r'(?<=__version__ = .)([\d\.]*)', f.read()).group(1)

with open('./README.md', 'r') as f:
    readme = f.read()


if __name__ == '__main__':
    setup(
        name='tinder-token',
        version=version,
        author='Zsolt Mester',
        author_email='',
        description='Python library for generating access tokens for using Tinder API, using Facebook or Phone authentication',
        long_description=readme,
        license='MIT',
        url='https://github.com/meister245/tinder-token',
        project_urls={
            "Code": "https://github.com/meister245/tinder-token",
            "Issue tracker": "https://github.com/meister245/tinder-token/issues",
        },
        packages=[
            'tinder_token'
        ],
        install_requires=[
            'requests'
        ],
        extras_require={
            'facebook': [
                'robobrowser',
                'html5lib',
                'Werkzeug==0.16.1'
            ]
        },
        include_package_data=True,
        scripts=[
            'scripts/tinder-token',
            'scripts/tinder-token.py'
        ]
    )
