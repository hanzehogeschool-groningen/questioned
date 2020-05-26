#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="Questioned",
    version="0.3.0",
    packages=find_packages(),
    include_package_data=True,

    author="David Visscher",
    author_email="pypi-dev@davidvisscher.nl",
    description="Computer Architectures Exam Generator",
    keywords="Exam question generator",

    python_requires='>=3.8',

    install_requires=[
        "click==7.1.1",
        "PyYAML==5.3.1"
    ],

    entry_points='''
        [console_scripts]
        qst=questioned:cli
    ''',

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research"
    ]
)
