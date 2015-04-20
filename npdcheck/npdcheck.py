# -*- coding: utf-8 -*-
"""
npdcheck is a style checker for module, class, and function / method
docstrings.

Usage:
    npdcheck.py FILE

Options:
    -h --help           # Show this screen.
    --version           # Show version.

.. note:: Deprecated warning
          This the the warning

Extended Summary
----------------
Nothing here yet

Parameters
----------
FILE : string
    The path to the file to be checked

Returns
-------
None

Yields
------
None

Other Parameters
----------------
None

Raises
------
None

See Also
--------
None

Notes
-----

References
----------

Examples
--------
>>> npdcheck("good_test_file.py")
Pass
>>> npdcheck("bad_test_file.py")
FAIL!

"""

from __future__ import print_function, division
from __future__ import absolute_import
#from __future__ import unicode_literals
from docopt import docopt

__author__ = "Douglas Thor"
__version__ = "v0.1.0"


def main():
    """ Main Code """
    docopt(__doc__, version=__version__)


if __name__ == "__main__":
    main()
