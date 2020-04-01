#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="Questioned",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,

    author="David Visscher",
    author_email="david@davidvisscher.nl",
    description="Computer Architectures Exam Generator",
    keywords="Exam question generator",

    install_requires=[
        "click==7.1.1",
        "PyYAML==5.3.1"
    ],

    entry_points='''
        [console_scripts]
        qst=questioned:cli
    '''
)
