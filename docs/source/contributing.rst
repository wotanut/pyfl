contributing
============
To contribue please open a pull request on the `GitHub repository <https://github.com/wotanut/pyfl>`_ with a summary of your changes.

Alternatively you can support me on `Ko-Fi <https://ko-fi.com/wotanut>`_ and watch me stream on `YouTube <https://www.youtube.com/channel/UCIVkp1F5JSyE0IKALyPW5sg>`_

.. important::
    Before you contribute it is highly recommended that you join the `Discord server <https://discord.gg/3Z2Q5Z9>`_ to discuss your changes with the community. Please **also** start a `discussion <https://github.com/wotanut/pyfl/discussions>`_ on the code you are working on. This will help you to avoid wasting your time on a pull request that somebody else has been working on.

How To Contribute
^^^^^^^^^^^^^^^^^

1. Fork the repository.
2. Make your changes.
3. Your code should automatically test itself on push back to GitHub. It should also build the documentation, please ensure your tests are passing before making a pull request as it will be instantly closed if they are not.
4. Make a pull request.


.. note:: 
    If, for whatever reason your tests are not passing on GitHub, you can run them locally. Please read below.

Running Tests Locally
^^^^^^^^^^^^^^^^^^^^^

1. Install the following packages.

.. code-block:: python

    pip3 install pytest
    pip3 install sphinx
    pip3 install sphinx_rtd_theme

2. Run ``pytest test_pyfl/test.py`` in the root directory.
3. Run ``sphinx-apidoc -f -o docs/source/ src/pyfl/`` in the route directory.
4. Run make html in the docs folder.

.. warning:: 
    Please ensure that you add your api key to the env file before running the tests. If you do not, the tests will fail.