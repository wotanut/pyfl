quickstart
==========

Installation
^^^^^^^^^^^^

To install the package, run the following command:

.. code-block:: python

   pip3 install pyfl


To install the development package run:

.. code-block:: python

   pip3 install git+https://github.com/wotanut/pyfl.git

.. warning:: 
    In order to install on windows please use pip instead of pip3

Synchornous Client Example
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import os
    import pyfl
    from pyfl.client import client

    key = os.getenv("api_key")

    TFL = pyfl.client(key)

    print(TFL.tube.get_line_status(TFL.helper.victoria))

Asynchronous Client Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
    The asynchronous client is not yet implemented.
   
You can check out the code in the `GitHub examples folder <https://github.com/wotanut/pyfl/tree/main/examples>`_