=============
PyCaw
=============

Welcome to PyCaw, the Cydia/Sileo package metadata python wrapper.

=============

Usage
===============

`get(type, id, value)`

The `type` parameter is basically asking for what you want to return. There are 6 possible types:

- `package`: Returns a package (**Requires `id` argument**)
- `packages`: Returns a complete list of all registered packages
- `repos`: Returns a list of verified repositories (AKA repos)
- `version`: Returns a list of all packages under version (id) (**Requires `id` argument**)
- `versions`: Returns a list of all iOS versions that are jailbroken
- `devices`: Returns a complete list of all devices

All packages that are registered with Cydia/Sileo are uniquely identified under `Reverse Domain Notation <https://en.wikipedia.org/wiki/Reverse_domain_name_notation>`_.

They typically follow this structure: 
`[domain_tld].[developer].[package_name]`

For example:

`me.nepeta.axon` -> **Axon by Nepeta**

You can get a specific package ID from the name of a package by using the `getIdFromName(name)` function. (It is case insensitive, so no need for capitalization)

For example, if we wanted to return the package ID of iFile:

>>> getIdFromName('ifile')
>>> eu.heinelt.ifile

Example
******************
Getting info for BetterCCXI:

>>> get('package', 'com.atwiiks.betterccxi')

This would return:

.. code-block:: python
{
    'id': 'com.atwiiks.betterccxi',
    'name': 'BetterCCXI',
    'latest': '1.4.10',
    'repository': 'Packix',
    'url': 'http://cydia.saurik.com/package/com.atwiiks.betterccxi/',
    'shortDescription': 'Enhance your control center on iOS 11 & 12',
    'category': 'Tweaks',
    'author': 'ATWiiks',
    'commercial': True,
    'date': '2018-06-28T13:55:34Z',
    'versions': [...]

}
