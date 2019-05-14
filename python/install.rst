Install
=======

Install Anaconda
----------------

Although macOS and most Linux distributions have their own pre-installed Python,
it's highly recommended to install the Anaconda distribution.

Download Anaconda from https://www.anaconda.com/distribution/
and following the install instruction for
`Windows <https://docs.anaconda.com/anaconda/install/windows/>`__,
`macOS <https://docs.anaconda.com/anaconda/install/mac-os/>`__,
and `Linux <https://docs.anaconda.com/anaconda/install/linux/>`__.

Install Packages
----------------

There're several different ways to install a Python package/library.
conda is the package manager provided by Anaconda, and pip is the built-in
pacakage manager provided by Python. When installing a package, it's recommended
to use conda first. If it's not found by conda, then use pip.

Using conda provided by Anaconda::

    conda install numpy

Using pip::

    pip install numpy

There're some situations you may want to install a Python package from source codes,
such as:

#. The package is not available from conda and pip, but its source codes are
   available on GitHub
#. Although the package is available from conda or pip, the source codes on GitHub
   are newer, with bugs fixed or new features added, but not released yet.

For such situations, you can install source codes from GitHub::

    pip install git+https://github.com/seisman/HinetPy.git

Or you can clone the source codes and run::

    python setup.py install

Upgrade Packages
----------------

Update via conda::

    conda update --all

Update via pip::

    pip install -U packagename
