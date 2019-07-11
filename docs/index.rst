PyCaw
=====

**Py**\ thon **C**\ ydia **A**\ PI **W**\ rapper

You can use PyCaw to retrieve information (JSON) of packages via the
Cydia/Sileo API. Data provided by `jlippold’s tweakCompatible`_

Getting started
---------------

Installation
~~~~~~~~~~~~

PyCaw can be installed with ``pip``. Simply run ``pip install pycaw``
and you’re done.

Usage
~~~~~

Using PyCaw is fairly easy syntax-wise.

**get(type, id, value)**

There are 6 possible ``type``\ s:

-  ``package``: Returns package data. Requires ``id`` arg.
-  ``packages``: Returns a list of *every single* package (5,000+). No
   args required.
-  ``repos``: Returns a list of verified repositories (URLS). No args
   required.
-  ``version``: Returns a list of packages compatible with given version
   (``id``). ``id`` arg required.
-  ``versions``: Returns a list of all jailbreak-able versions. No args
   required.
-  ``devices``: Returns a list of all devices that are jailbreak-able.

Getting a package
^^^^^^^^^^^^^^^^^

Getting a package is also fairly easy, and only takes 1 line.

How packages are identified
'''''''''''''''''''''''''''

Before actually running the function, you need to understand how
packages are identified if you don’t already. Any application running on
iOS is identified by `Reverse Domain Name Notation`_ (AKA Bundle ID).
This identification structure typically follows this pattern:

``[domain_tld].[developer].[package_name]``

For example, Instagram’s Bundle ID is ``com.burbn.instagram``.

The popular tweak iFile’s Bundle ID is ``eu.heinelt.ifile``.

If you don’t know the Bundle ID of a package, run
``getIdFromName(name)``. It returns the Bundle ID of a package, which
can in turn be used in the ``get()`` function that we’re about to go
over.

Example: Returning a Bundle ID
''''''''''''''''''''''''''''''

In this example, we are returning the Bundle ID of Axon, a package by
Nepeta. **The ``name`` argument is case insensitive, so don’t worry
about capitalization**.

.. code:: python

   pycaw.getIdFromName('axon')

Returns

::

   me.nepeta.axon

Example: Returning a package with ``get()``
'''''''''''''''''''''''''''''''''''''''''''

In this example, we are returning tweakCompatible by jlippold.

.. code:: python

   pycaw.get('package', 'bz.jed.tweakcompatible')

Returns

.. code:: python

   {
       'id': 'bz.jed.tweakcompatible',
       'name': 'tweakCompatible',
       'latest': '0.1.5',
       'repository': 'BigBoss',
       'url': 'http://cydia.saurik.com/package/bz.jed.tweakcompatible/',
       'shortDescription': 'Adds a way to check tweak compatibility in cydia',
       'category': 'Tweaks',
       'author': 'treAson',
       'commercial': False,
       'versions': [ ... ]
   }

The ``get()`` response explained
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

================ =============================================
Name             Description
================ =============================================
id               Bundle ID
name             Name
latest           Latest version
repository       Repository where the package can be found
url              Cydia URL
shortDescription Description of package
category         Category (Tweaks, System, etc…)
author           Author
commercial       Indicating whether or not the package is paid
versions         Dictionary of versions (and their reviews)
================ =============================================

The ``value`` argument
''''''''''''''''''''''

The ``value`` argument in the ``get()`` function is optional, and can
return the specified value in which you want to return from the
``get()`` response.

Example: Using the ``value`` argument
'''''''''''''''''''''''''''''''''''''

In this example, we return the latest version of Nepeta’s FlashyHUD (as
of now):

.. code:: python

   pycaw.get('package', 'me.nepeta.flashyhud', 'latest')

Returns

::

   0.2.2

Docs are still under construction as of 7/10/2019.
''''''''''''''''''''''''''''''''''''''''''''''''''

.. _jlippold’s tweakCompatible: https://jlippold.github.io/tweakCompatible/
.. _Reverse Domain Name Notation: https://en.wikipedia.org/wiki/Reverse_domain_name_notation