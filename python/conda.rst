Using conda
===========

Config
------

Add `conda-forge` channel::

    conda config --add channels conda-forge

Update
------

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
