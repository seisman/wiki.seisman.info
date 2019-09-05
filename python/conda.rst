Using conda
===========

conda is the package manager provided by Anaconda.

Configuration
-------------

conda is ready to use after installing Anaconda. You don't have to configure it.

For customization or better perform, you can configure it by running commands
like ``conda config ...``, or you can directly edit the configuration file,
which usually is ``~/.condarc``.

Anaconda's builtin channel is ``default``, which contains several thousands of pacakges.
`conda-forge <http://conda-forge.org/>`_ is another channel maintained by community,
which also contains several thousands of packages not included in the ``default``
channel. It's fortunate that ``conda-forge`` is compatible with ``default``.
It's a good idea to add ``conda-forge`` channel, so you have more packages available.

    conda config --add channels conda-forge
    conda config --set channel_priority strict

Update via conda
----------------

::

    # Update conda
    conda update conda

    # Update Anaconda
    conda update anaconda

    # List all installed modules
    conda list

    # Update all installed modules
    conda update --all

Virtual Environment
-------------------

::

    # Create an virtual environment
    conda create --name envname
    conda create --name envname python=3.6 astroid babel

    # Activate an environment
    source activate snowflakes

    # Deactivate/Exit an environment
    source deactivate

    # List all environments
    conda info --envs

    # Delete an environment
    conda env remove --name xxxx
