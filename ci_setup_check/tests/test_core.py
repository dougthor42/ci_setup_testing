from __future__ import print_function, division
#from __future__ import absolute_import
import unittest

# NoseTest OK/Fail
### Absolute import Y/N                  N               Y
# -------------------------------------------------------------
import ci_setup_check.core as core     # OK              OK
#from .. import core as core            # OK              OK
#from . import core as core             # fail            fail
#from ci_setup_check import core        # OK              OK
#import core                            # fail           fail


class Examples(unittest.TestCase):
    def test_things(self):
        result = core.func(2, 3)
        self.assertEqual(result, 5)
