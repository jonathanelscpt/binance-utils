binance-utils Overview
======================

Simple CLI reporting utility for binance account information


Installation
------------

Virtual environment setup for linux:

.. code-block:: bash

    $ python3 -m venv venv
    $ source venv/bin/activate

Virtual environment setup for windows:

.. code-block:: bash

    $ python3 -m venv venv
    $ venv\Scripts\activate


Install package from local source:

.. code-block:: bash

    $ pip install -e .


Authentication
--------------

Add your binance api key and secret as environment variables.

In linux:

.. code-block:: bash

    # Set these values in your ~/.zprofile (zsh) or ~/.profile (bash)
    $ export BINANCE_KEY=key
    $ export BINANCE_SECRET=secret


In Windows:

.. code-block:: PowerShell

    $ set BINANCE_KEY=key
    $ set BINANCE_SECRET=secret



Execution
---------

To run the cli utility and fetch account balances

.. code-block:: bash

    $ binance-utils

