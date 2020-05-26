.. _installation-guide:
Installation Guide
==================

Questioned can be installed as a package from PyPI as well as from source.

Using pip
---------
In order to install from PyPI using pip, simply run the following:
::
    $ pip install questioned


From Source
-----------
In order to install questioned from source, follow these steps:

Clone the project repository and enter it:
::
    git clone git@github.com:DavidVisscher/questioned.git
    cd questioned

To install system-wide, it may be simply installed with:
::
    python3 setup.py install

Otherwise, a script has been provided which automatically sets up a development
environment. This script installs the editable version in a local virtualenv.
::
    source devsetup.sh
