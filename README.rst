numpydoclint
============
A style checker for docstrings that are supposed to follow the numpy docstring
conventions (https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt)

Goal
----
The goal of `numpydoclint` is to checks each docstring within a module for
conformance to numpydoc standards.

`numpydoclint` checks that docstrings have all of the required sections:

- 1.  Short Summary
- 4.  Parameters
- 5.  Returns  or  6. Yields

and checks for optional sections:

- 2.  Depreciation Warning
- 3.  Extended Summary
- 7.  Other Parameters
- 8.  Raises
- 9.  See Also
- 10. Notes
- 11. References
- 12. Examples

`numpydoclint` should also check for the following:

- Line limit of 75 characters including whitespace (See last paragraph of https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt#docstring-standard)

This module will also support class documentation and module documentation.

Installation
------------

To be added to PyPI later, so you'll be able to run

``pip install numpydoclint``

Usage
-----

Simply call numpydoclint with the file in question as the first arguement:

``>>> python numpydoclint "C:\myfile.py"``

Changelog:
----------

See docs/changelog.rst
